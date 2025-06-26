from app import db

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    reminders = db.relationship('Reminder', backref='plant', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Plant {self.name}>'
