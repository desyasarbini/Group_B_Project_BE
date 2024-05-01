from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controller.admin_controller import (
    create_admin, 
    do_admin_login,
    get_admin,  
    delete_admin,
    admin_logout)

admin_blueprint = Blueprint('admin_endpoint', __name__)

admin_blueprint.route("/admin/<id>", methods=["GET"])(get_admin)

admin_blueprint.route("/admin", methods=["POST"])(create_admin)

admin_blueprint.route("/admin/login", methods=["POST"])(do_admin_login)

admin_blueprint.route("/admin/<id>", methods=["DELETE"])(delete_admin)

admin_blueprint.route("/admin/logout", methods=["GET"])(jwt_required()(admin_logout))