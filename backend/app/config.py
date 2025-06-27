import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# Go up one level to the `backend` directory to find the .env file
dotenv_path = os.path.join(os.path.dirname(basedir), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/green_thumb_db'