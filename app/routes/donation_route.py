from flask import Blueprint
from app.controller.donation_controller import (
    create_donation
)

donation_blueprint = Blueprint('donation_endpoint', __name__)

donation_blueprint.route("/donation/create", methods=["POST"])(create_donation)