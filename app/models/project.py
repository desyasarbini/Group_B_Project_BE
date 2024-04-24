from app.utils.database import db
from sqlalchemy import func


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    image = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(655), nullable=False)
    target_amount = db.Column(db.DECIMAL(10,2), nullable=False)
    collected_amount = db.Column(db.DECIMAL(10,2))
    start_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    end_date = db.Column(db.DateTime(timezone=True), nullable=False)
    percentage = db.Column(db.Float(precision=2))

    admin = db.relationship("Admin")

    def serialize(self):
        return {
            'id' : self.id,
            'admin_id' : self.admin_id,
            'image' : self.image,
            'title' : self.title,
            'description' : self.description,
            'target_amount' : self.target_amount,
            'collected_amount' : self.collected_amount,
            'start_date' : self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            'end_date' : self.end_date,
            'percentage' : self.percentage
        }

    def __repr__(self):
        return f'<Project{self.id}>'
