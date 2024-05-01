from flask import Blueprint
from app.controller.donatur_controller import (
    create_donatur,
    get_donatur_detail
    )

donatur_blueprint = Blueprint('donatur_endpoint', __name__)

donatur_blueprint.route("/donatur-create", methods=["POST"])(create_donatur)

donatur_blueprint.route("/donatur/<donatur_id>", methods=["GET"])(get_donatur_detail)