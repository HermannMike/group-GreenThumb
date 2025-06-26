from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Change this to your actual database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import models to register them with SQLAlchemy
    from backend import plant_model
    from backend import reminder_model
    from backend import user_model
    
    # You can add blueprints or routes here if needed
    
    return app
