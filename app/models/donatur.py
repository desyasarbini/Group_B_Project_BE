from app.utils.database import db

class Donatur(db.Model):
    __tablename__ = "donatur"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'id' : self.id,
            'email' : self.email,
            'phone_number' : self.phone_number
        }

    def __repr__(self):
        return f'<Donatur{self.email}>'