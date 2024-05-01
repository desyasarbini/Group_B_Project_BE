# from flask_jwt_extended import get_jwt_identity
from app.models.donatur import Donatur
from app.utils.database import db
from app.utils.api_response import api_response
from app.connector.sql_connector import engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify, request

def create_donatur():
    # current_donatur_id = get_jwt_identity()
    email = request.json.get("email")
    phone_number = request.json.get("phone_number")

    new_donatur = Donatur(email = email, phone_number=phone_number)

    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    session.begin()
    try:
        session.add(new_donatur)
        session.commit()
    except Exception as e:
        print(f"error during registration: {e}")
        session.rollback()
        return {"message": "Create donatur failed"}
    return api_response(
        status_code = 201, 
        message = "Create donatur success!", 
        data = {"id": new_donatur.id, "email": new_donatur.email, "phone_number": new_donatur.phone_number}
    )

def get_donatur_detail(id):
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    session.begin()
    try:
        donatur = session.query(Donatur).filter(Donatur.id == id).first()
        if donatur:
            return jsonify(donatur.serialize)
        else:
            return jsonify({
                "message" : 'donatur not found' 
            })
    except Exception as e:
        session.rollback()
        return (f"get donatur detail failed: {e}")