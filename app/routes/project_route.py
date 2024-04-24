from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controller.project_controller import (create_project)

project_blueprint = Blueprint('project_endpoint', __name__)

project_blueprint.route("/project-create", methods=["POST"])(jwt_required()(create_project))