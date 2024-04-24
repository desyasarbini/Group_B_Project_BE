# from flask_jwt_extended import get_jwt_identity
from app.models.donatur import Donatur
from app.utils.database import db
from app.utils.api_response import api_response
from flask import jsonify, request

def create_donatur():
    # current_donatur_id = get_jwt_identity()
    email = request.form['email']
    phone_number = request.form['phone_number']

    new_donatur = Donatur(email = email, phone_number=phone_number)

    db.session.begin()
    try:
        db.session.add(new_donatur)
        db.session.commit()
    except Exception as e:
        print(f"error during registration: {e}")
        db.session.rollback()
        return {"message": "Create donatur failed"}
    return api_response(
        status_code = 201, 
        message = "Create donatur success!", 
        data = {"id": new_donatur.id, "email": new_donatur.email, "phone_number": new_donatur.phone_number}
    )