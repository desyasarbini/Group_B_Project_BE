from app.models.admin import Admin
from app.utils.database import db
from app.utils.api_response import api_response
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, create_access_token

def get_admin(id):
    db.session.begin()
    try:
        admin = db.session.query(Admin).filter((Admin.id==id)).first()
        if admin:
            return jsonify(admin.serialize(full=True))
        else:
            return jsonify({
                "message" : 'admin not register yet' 
            })
    except Exception as e:
        print(f"Error during registration: {e}")
        db.session.rollback()
        return {"message": "admin not found"}


def create_admin():
    username = request.form['username']
    password = request.form['password']

    new_admin = Admin(username = username)
    new_admin.set_password(password)

    db.session.begin()
    try:
        db.session.add(new_admin)
        db.session.commit()
    except Exception as e:
        print(f"error during registration: {e}")
        db.session.rollback()
        return {"message": "Create admin failed"}
    return api_response(
        status_code = 201, 
        message = "Create admin success!", 
        data = {"id": new_admin.id, "username": new_admin.username}
    )

def do_admin_login():
    username = request.form['username']
    password = request.form['password']

    db.session.begin()
    try:
        admin = db.session.query(Admin).filter(Admin.username == username).first()
        
        if admin == None:
            return api_response(
                status_code = 404,
                message = "username not found",
                data = {}
            )
        
        if not admin.check_password(password):
            return api_response(
                status_code = 404,
                message = "password incorrect, please check again",
                data = {}
            )

        access_token = create_access_token(identity=admin.id)

        return api_response(
            status_code = 200,
            message = "Login successfully",
            data = {"admin": admin.serialize(full = False), "access_token": access_token}
        )
    except Exception as e:
        print(f"Error during login: {e}")
        db.session.rollback()
        return {"message": "Login failed"}

def protected_route():
    current_user = get_jwt_identity()
    return api_response(
        status_code = 200,
        message = {"login as id": current_user},
        data = {}
    )

def admin_logout():
    current_user = get_jwt_identity()
    return api_response(
        status_code = 200,
        message = {"Logged out successfully for id": current_user},
        data = {}
    )