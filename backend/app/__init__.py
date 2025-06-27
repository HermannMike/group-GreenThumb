from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # The database session will be managed elsewhere, not directly in the app factory
    from app.models.user import User
    from app.models.plant import Plant
    from app.models.reminder import Reminder

    return app