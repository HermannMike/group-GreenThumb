from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
import logging

db = SQLAlchemy()
migrate = Migrate()


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

logging.basicConfig(level=logging.INFO)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # The database session will be managed elsewhere, not directly in the app factory
    from app.models.user import User
    from app.models.plant import Plant
    from app.models.reminder import Reminder

    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            logging.info('Signup attempt with missing username or password')
            return jsonify({'message': 'Username and password required'}), 400
        if User.query.filter_by(username=username).first():
            logging.info(f'Signup attempt with existing username: {username}')
            return jsonify({'message': 'Username already exists'}), 400
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        logging.info(f'User signed up: {username}')
        return jsonify({'message': 'User created successfully'}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            logging.info('Login attempt with missing username or password')
            return jsonify({'message': 'Username and password required'}), 400
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            logging.info(f'Failed login attempt for username: {username}')
            return jsonify({'message': 'Invalid username or password'}), 401
        logging.info(f'User logged in: {username}')
        return jsonify({'message': 'Login successful'}), 200

    return app
