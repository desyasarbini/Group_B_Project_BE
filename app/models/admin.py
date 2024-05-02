from app.models.base import Base
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import String, Integer
import bcrypt

class Admin(Base):
    __tablename__ = "admin"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(20), nullable=False, unique=True)
    password = mapped_column(String(20), nullable=False)

    projects = relationship("Project", back_populates="admin")

    def serialize(self, full=True):
        if full:
            return {
                'id': self.id,
                'username': self.username,
                'password': self.password
            }
        else:
            return {
                'id': self.id,
                'username': self.username
            }

    def __repr__(self):
        return f'<Admin{self.username}>'

    # u/ encrypt password
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # u/ check password yg ter-encrypt
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))