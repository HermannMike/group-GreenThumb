from backend import create_app, db
from backend.app.models.user import User  # Example model import

def test_app():
    app = create_app()
    app.app_context().push()
    
    # Test database connection and create tables
    db.create_all()
    print("Database tables created successfully.")
    
    # Test CRUD operation example
    user = User(username='testuser', email='test@example.com')
    db.session.add(user)
    db.session.commit()
    print("User added to database successfully.")
    
    # Query the user
    queried_user = User.query.filter_by(username='testuser').first()
    if queried_user:
        print(f"Queried User: {queried_user.username}, {queried_user.email}")
    else:
        print("User query failed.")
    
    # Clean up
    db.session.delete(queried_user)
    db.session.commit()
    print("User deleted from database successfully.")

if __name__ == '__main__':
    test_app()
