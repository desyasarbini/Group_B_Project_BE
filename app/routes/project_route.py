from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controller.project_controller import (
    create_project,
    delete_project,
    project_detail,
    get_all_project,
    update_project
    )

project_blueprint = Blueprint('project_endpoint', __name__)

project_blueprint.route("/project-create", methods=["POST"])(jwt_required()(create_project))

project_blueprint.route("/project/update/<project_id>", methods=["PUT"])(jwt_required()(update_project))

project_blueprint.route("/project/delete/<project_id>", methods=["DELETE"])(jwt_required()(delete_project))

project_blueprint.route("/project-detail/<project_id>", methods=["GET"])(project_detail)

project_blueprint.route("/project", methods=["GET"])(get_all_project)