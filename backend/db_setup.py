from sqlalchemy import create_engine
from app.models.base import Base
from app.config import Config

def setup_database():
    """
    Creates the database and all tables defined in the models.
    """
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)
    print("Database and tables created successfully.")

if __name__ == '__main__':
    setup_database()