from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    species = Column(String(100), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='plants')
    reminders = relationship('Reminder', back_populates='plant', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Plant {self.name}>'
