from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controller.admin_controller import (
    create_admin, 
    do_admin_login,
    protected_route,
    get_admin,
    protected_route,
    admin_logout)

admin_blueprint = Blueprint('admin_endpoint', __name__)

admin_blueprint.route("/admin/<id>", methods=["GET"])(get_admin)

admin_blueprint.route("/admin", methods=["POST"])(create_admin)

admin_blueprint.route("/admin/login", methods=["POST"])(do_admin_login)

admin_blueprint.route("/protected", methods=["GET"])(jwt_required()(protected_route))

admin_blueprint.route("/admin/logout", methods=["GET"])(jwt_required()(admin_logout))


# @admin_blueprint.route("/<int:admin_id>", methods=["PUT"])
# def update_admin():
#     return "update admin"

    
# @admin_blueprint.route("/<int:admin_id>", methods=["DELETE"])
# def delete_admin():
#     return "delete admin"