from datetime import datetime
from pydantic import ValidationError
from app.models.donation import Donation
from app.models.project import Project
from app.utils.api_response import api_response
from app.connector.sql_connector import Session
from app.validations.donation_validation import DonationCreate
from flask import jsonify, request

def donation_detail(donation_id):
    session = Session()
    session.begin()
    try:
        donation = session.query(Donation).filter(Donation.id == donation_id).first()
        if donation:
            return api_response(
                status_code=200,
                message="get donation detail success!",
                data={
                    'id': donation.id,
                    'email': donation.email,
                    'amount': donation.amount                    
                }
            )
        else:
            return jsonify({
                "message" : 'donation not found' 
            })
    except Exception as e:
        session.rollback()
        return jsonify({"message": "error lagi bung untuk donation detail yak!"})
    finally:
        session.close()

def create_donation():
    try:
        donation_data = DonationCreate(**request.json)
    except ValidationError as e:
        return jsonify(f"Validation error occurred: {e}")

    project_id = donation_data.project_id
    email = donation_data.email
    phone_number = donation_data.phone_number
    amount = donation_data.amount
    donation_date = datetime.now()

    session = Session()
    try:
        session.begin()
        project = session.query(Project).filter(Project.id==project_id).first()
        if project is None:
            return api_response(
                status_code=400,
                message="Project not found, choose another project",
                data={}
            )

        start_donation = Donation(
            project_id = project_id,
            email = email,
            phone_number = phone_number,
            amount = amount,
            donation_date = donation_date
        )
        
        session.add(start_donation)
        session.commit()

        return api_response(
            status_code=200,
            message="create donation successfully, thank you",
            data={
                'id': start_donation.id,
                'project_id': start_donation.project_id,
                'email': start_donation.email,
                'phone_number': start_donation.phone_number,
                'amount': start_donation.amount,
                'donation_date': start_donation.donation_date
            }
        )
    except Exception as e:
        session.rollback()
        return jsonify({"error": f"Failed to create donation: {str(e)}"})
    finally:
        session.close()
