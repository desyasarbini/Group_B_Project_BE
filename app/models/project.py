from app.models.base import Base
from sqlalchemy import String, Integer, DECIMAL, DateTime, Float, ForeignKey, func
from sqlalchemy.orm import relationship, mapped_column

class Project(Base):
    __tablename__ = "project"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    admin_id = mapped_column(Integer, ForeignKey('admin.id', ondelete="CASCADE"))
    project_image = mapped_column(String(525), nullable=False)
    project_name = mapped_column(String(255), nullable=False)
    description = mapped_column(String(866), nullable=False)
    target_amount = mapped_column(DECIMAL(12,2), default=0.00, nullable=False)
    collected_amount = mapped_column(DECIMAL(12,2), default=0.00, nullable=False)
    percentage = mapped_column(DECIMAL(3,2), default=0.00, nullable=False)
    start_date = mapped_column(DateTime(timezone=True), server_default=func.now())
    end_date = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now())

    donations = relationship("Donation", back_populates="to_project")
    admin = relationship("Admin", back_populates="projects")

    def serialize(self, full=True):
        if full:
            return {
                'id': self.id,
                'project_image': self.project_image,
                'project_name' : self.project_name,
                'description' : self.description,
                'target_amount' : self.target_amount,
                'collected_amount' : self.collected_amount,
                'start_date' : self.start_date,
                'end_date' : self.end_date,
                'percentage' : self.percentage,
                'updated_at' : self.updated_at
            }
        else:
            return {
                'id' : self.id,
                'admin_id' : self.admin_id,
                'project_image' : self.project_image,
                'project_name' : self.project_name,
                'description' : self.description,
                'target_amount' : self.target_amount,
                'collected_amount': self.collected_amount,
                'percentage' : f"{self.percentage: .2f}",
                'end_date' : self.end_date
            }

    def __repr__(self):
        return f'<Project{self.id}>'
    
    def percent_calculation(self):
        if self.target_amount != 0:
            self.percentage = (self.collected_amount / self.target_amount) * 100
        else:
            self.percentage = 0.00