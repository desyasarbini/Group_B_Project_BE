# from app.utils.database import db
from app.models.base import Base
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import String, Integer

class Donatur(Base):
    __tablename__ = "donatur"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    email = mapped_column(String(255), nullable=False)
    phone_number = mapped_column(String(50), nullable=False)

    donations = relationship("Donation", back_populates="from_donatur")

    def serialize(self):
        return {
            'id' : self.id,
            'email' : self.email,
            'phone_number' : self.phone_number
        }

    def __repr__(self):
        return f'<Donatur{self.email}>'