from app.models.project import Project
from app.utils.database import db
from app.utils.api_response import api_response
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, create_access_token

def create_project():
    image = request.form['image']
    title = request.form['title']
    description = request.form['description']
    target_amount = request.form['target_amount']
    end_date = request.form['end_date']

    new_project = Project (
        image = image,
        title = title,
        description = description,
        target_amount = target_amount,
        end_date = end_date
    )

    db.session.begin()
    try:
        db.session.add(new_project)
        db.session.commit()
    except Exception as e:
        print(f"error during create project: {e}")
        db.session.rollback()
        return {"message": "add new project failed"}
    return api_response(
        status_code = 201, 
        message = "Create project success!", 
        data = {
            "id": new_project.id,
            "admin_id": new_project.admin_id,
            "image": new_project.image,
            "title": new_project.title,
            "description": new_project.description,
            "target_amount": new_project.target_amount,
            "end_date": new_project.end_date
            }
    )
