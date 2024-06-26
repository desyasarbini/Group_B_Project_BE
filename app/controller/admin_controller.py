from pydantic import ValidationError
from app.models.admin import Admin
from app.utils.api_response import api_response
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, create_access_token
from app.connector.sql_connector import Session
from app.validations.admin_validation import AdminCreate, AdminLogin

def create_admin():
    # validation start
    try:
        admin_data = AdminCreate(**request.json)
    except ValidationError as e:
        return jsonify(f"Validation error occurred: {e}")

    username = admin_data.username
    password = admin_data.password
    # validation end

    session = Session()
    
    existing_admin = session.query(Admin).filter(Admin.username == username).first()
    if existing_admin:
        return jsonify(f"Username '{username}' already exists. Please choose a different username.")

    new_admin = Admin(username = username)
    new_admin.set_password(password)

    session.begin()
    try:
        session.add(new_admin)
        session.commit()
        session.refresh(new_admin)
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
    # validation start
    try:
        login_data = AdminLogin(**request.json)
    except ValidationError as e:
        return jsonify(f"Validation error occurred: {e}")
    # validation end
    
    username = login_data.username
    password = login_data.password

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

def get_all_admin():
    response_data = dict()
    session = Session()
    session.begin()
    try:
        admin_query = session.query(Admin)
        if request.args.get('query') != None:
            search_query = request.args.get('query')
            admin_query = admin_query.filter(Admin.username.like(f"%{search_query}%"))
        
        admins = admin_query.all()
        response_data['admins'] = [admin.serialize(full=False) for admin in admins]
        return jsonify(response_data)

    except Exception as e:
        session.rollback()
        return jsonify(f"get all admin failed: {e}")
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