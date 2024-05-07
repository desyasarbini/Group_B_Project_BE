from sqlalchemy import func
from app.models.admin import Admin
from app.models.project import Project
from app.connector.sql_connector import Session
from app.utils.api_response import api_response
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity

def create_project():
    current_admin_id = get_jwt_identity()
    session = Session()

    session.begin()

    admin = session.query(Admin).filter(Admin.id == current_admin_id).first()
    if admin is None:
        return jsonify({"message": "You don't have permission to create a project"}), 403

    project_image = request.json.get("project_image", None)
    project_name = request.json.get("project_name", None)
    description = request.json.get("description", None)
    target_amount = float(request.json.get("target_amount", None))
    end_date = request.json.get("end_date", None)

    new_project = Project (
        admin_id = current_admin_id,
        project_image = project_image,
        project_name = project_name,
        description = description,
        target_amount = target_amount,
        end_date = end_date
    )

    try:
        session.add(new_project)
        session.commit()
        
        new_project.percent_calculation()
    except Exception as e:
        session.rollback()
        return (f"login failed: {e}")
    finally:
        session.expunge_all()
        session.close()
    return api_response(
        status_code = 201, 
        message = "Create project success!", 
        data = {
            "id": new_project.id,
            "admin_id": new_project.admin_id,
            "project_image": new_project.project_image,
            "project_name": new_project.project_name,
            "description": new_project.description,
            "target_amount": new_project.target_amount,
            "end_date": new_project.end_date,
            "percentage": new_project.percentage
        }
    )

def get_all_project():
    response_data = dict()
    session = Session()
    session.begin()
    try:
        project_query = session.query(Project)

        if request.args.get('query') != None:
            search_query = request.args.get('query')
            project_query = project_query.filter(Project.project_name.like(f"%{search_query}%"))

        projects = project_query.all()
        response_data['projects'] = [project.serialize(full=False) for project in projects]
        return jsonify(response_data)

    except Exception as e:
        session.rollback()
        return jsonify(f"get all project failed: {e}")
    finally:
        session.close()

def project_detail(project_id):
    session = Session()
    session.begin()
    try:
        project = session.query(Project).filter((Project.id==project_id)).first()
        if project:
            return jsonify(project.serialize(full=True))
        else:
            return jsonify({
                "message": "project not found"
            })
    except Exception as e:
        session.rollback()
        return jsonify(f"error nya disini yak! : {e}")
    finally:
        session.close()

def delete_project(project_id):
    session = Session()
    session.begin()
    try:

        project_to_delete = session.query(Project).filter(Project.id==project_id).first()

        if project_to_delete is None:
            return jsonify({"message": "project not found"}), 404

        session.delete(project_to_delete)
        session.commit()
        
        return jsonify({"message": "succefully delete project"})
    except Exception as e:
        session.rollback()
        return jsonify(f"delete project failed: {e}"), 500
    finally:
        session.close()

def update_project(project_id):
    session = Session()
    session.begin()
    try:
        project_to_update = session.query(Project).filter(Project.id==project_id).first()

        project_to_update.project_name = request.json.get('project_name', project_to_update.project_name)
        project_to_update.description = request.json.get('description', project_to_update.description)
        project_to_update.end_date = request.json.get('end_date', project_to_update.end_date)
        project_to_update.updated_at = func.now()

        session.commit()
        return api_response(
            status_code=200,
            message="update project success!",
            data={
                'project_name': project_to_update.project_name,
                'description': project_to_update.description,
                'end_date': project_to_update.end_date,
                'updated_at': project_to_update.updated_at
            }
        )
    except Exception as e:
        session.rollback()
        return jsonify(f"update project failed: {e}"), 500
    finally:
        session.close()