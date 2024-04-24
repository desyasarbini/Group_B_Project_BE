from flask import Blueprint
from app.controller.donatur_controller import (create_donatur)

donatur_blueprint = Blueprint('donatur_endpoint', __name__)

donatur_blueprint.route("/donatur", methods=["POST"])(create_donatur)