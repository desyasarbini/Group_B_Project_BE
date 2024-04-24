from app.utils.database import db
import bcrypt

class Admin(db.Model):
    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)

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
        return f'<User{self.username}>'

    # u/ encrypt password
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # u/ check password yg ter-encrypt
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))