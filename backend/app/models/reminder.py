from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    reminder_type = Column(String(50), nullable=False)
    frequency = Column(String(50), nullable=False)
    plant_id = Column(Integer, ForeignKey('plants.id'), nullable=False)

    plant = relationship('Plant', back_populates='reminders')

    def __repr__(self):
        return f'<Reminder {self.reminder_type} for plant {self.plant_id}>'
