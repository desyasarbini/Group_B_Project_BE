from app.models.base import Base
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import Integer, String, DECIMAL, DateTime, ForeignKey, func

class Donation(Base):
    __tablename__ = "donation"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id = mapped_column(Integer, ForeignKey('project.id'))
    email = mapped_column(String(100), nullable=False)
    phone_number = mapped_column(String(20), nullable=False)
    amount = mapped_column(DECIMAL(12,2), nullable=False )
    donation_date = mapped_column(DateTime(timezone=True), server_default=func.now())

    to_project = relationship("Project", back_populates="donations")

    def serialize(self):
        return {
            'id' : self.id,
            'project_id' : self.project_id,
            'email' : self.email,
            'phone_number' : self.phone_number,
            'amount' : self.amount,
            'donation_date' : self.donation_date
        }

    def __repr__(self):
        return f'<Donation{self.id}>'