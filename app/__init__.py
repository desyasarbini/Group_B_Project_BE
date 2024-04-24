from flask import Flask
from dotenv import load_dotenv
from app.utils.database import db, migrate
from app.routes.admin_route import admin_blueprint
from app.routes.donatur_route import donatur_blueprint
from app.routes.project_route import project_blueprint
from flask_jwt_extended import JWTManager
import os

load_dotenv()

app = Flask(__name__)

db_type = os.getenv('DATABASE_TYPE')
db_host = os.getenv('DATABASE_HOST')
db_name = os.getenv('DATABASE_NAME')
db_port = os.getenv('DATABASE_PORT')
db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = f"{db_type}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)

jwt = JWTManager(app)

db.init_app(app)
@app.route("/")
def helloWorld():
    return "hello world"

app.register_blueprint(admin_blueprint)
app.register_blueprint(donatur_blueprint)
app.register_blueprint(project_blueprint)