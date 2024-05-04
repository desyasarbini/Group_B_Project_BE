from app.models.base import Base
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import Integer, DECIMAL, DateTime, ForeignKey, func

class Donation(Base):
    __tablename__ = "donation"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id = mapped_column(Integer, ForeignKey('project.id'))
    donatur_id = mapped_column(Integer, ForeignKey('donatur.id'))
    amount = mapped_column(DECIMAL(12,2))
    donation_date = mapped_column(DateTime(timezone=True), server_default=func.now())

    to_project = relationship("Project", back_populates="donations")
    from_donatur = relationship("Donatur", back_populates="donations")

    def serialize(self):
        return {
            'id' : self.id,
            'project_id' : self.project_id,
            'donatur_id' : self.donatur_id,
            'amount' : self.amount,
            'donation_date' : self.donation_date
        }

    def __repr__(self):
        return f'<Donation{self.id}>'