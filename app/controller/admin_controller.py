from app.models.admin import Admin
from app.utils.api_response import api_response
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, create_access_token
from app.connector.sql_connector import engine, Session
from sqlalchemy.orm import sessionmaker

def create_admin():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    new_admin = Admin(username = username)
    new_admin.set_password(password)

    session = Session()
    session.begin()
    try:
        session.add(new_admin)
        session.commit()
    except Exception as e:
        session.rollback()
        return jsonify(f"create admin failed: {e}")
    finally:
        session.close()
    return api_response(
        status_code = 201, 
        message = "Create admin success!", 
        data = {"id": new_admin.id, "username": new_admin.username}
    )

def do_admin_login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    session = Session()
    session.begin()
    try:
        admin = session.query(Admin).filter(Admin.username == username).first()
        
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
        session.rollback()
        return jsonify(f"login failed: {e}")
    finally:
        session.close()

def get_admin(id):
    session = Session()
    session.begin()
    try:
        admin = session.query(Admin).filter((Admin.id==id)).first()
        if admin:
            return jsonify(admin.serialize(full=True))
        else:
            return jsonify({
                "message" : 'admin not register yet' 
            })
    except Exception as e:
        session.rollback()
        return jsonify(f"get admin failed: {e}")
    finally:
        session.close()

def admin_logout():
    current_user = get_jwt_identity()
    return api_response(
        status_code = 200,
        message = {"Logged out successfully for id": current_user},
        data = {}
    )

def delete_admin(id):
    session = Session()
    session.begin()
    try:
        admin_to_delete = session.query(Admin).filter(Admin.id == id).first()
        if admin_to_delete is None:
            return jsonify({"message": "admin not found"}), 404
        
        session.delete(admin_to_delete)
        session.commit()

        return {'message': 'Admin deleted successfully'}
    except Exception as e:
        session.rollback()
        return jsonify(f"delete admin failed: {e}")
    finally:
        session.close() 