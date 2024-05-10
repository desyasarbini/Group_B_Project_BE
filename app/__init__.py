import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app.routes.admin_route import admin_blueprint
from app.routes.project_route import project_blueprint
from app.routes.donation_route import donation_blueprint

load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)
CORS(app, origins=['http://localhost:3000', 'https://group-b-project-fe-git-main-desyasarbinis-projects.vercel.app/', 'https://www.luv2read.site/'], supports_credentials=True)

@app.route("/")
def helloWorld():
    return "hello world, berhasil terhubung ke db"

app.register_blueprint(admin_blueprint)
app.register_blueprint(project_blueprint)
app.register_blueprint(donation_blueprint)

if __name__ == "__main__":
    app.run()