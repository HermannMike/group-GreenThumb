from app import db

class Reminder(db.Model):
    __tablename__ = 'reminders'

    id = db.Column(db.Integer, primary_key=True)
    reminder_type = db.Column(db.String(50), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)

    def __repr__(self):
        return f'<Reminder {self.reminder_type} for plant {self.plant_id}>'
