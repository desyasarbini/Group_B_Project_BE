from app.models.donation import Donation
from app.models.project import Project
# from app.models.donatur import Donatur
from app.utils.api_response import api_response
from app.connector.sql_connector import Session
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
    project_id = request.json.get("project_id", None)
    email = request.json.get("email", None)
    phone_number = request.json.get("phone_number", None)
    amount = request.json.get("amount", None)
    donation_date = request.json.get("donation_date")

    session = Session()
    try:
        session.begin()

        # donatur = session.query(Donatur).filter(Donatur.id==donatur_id).first()
        project = session.query(Project).filter(Project.id==project_id).first()
        # if donatur is None:
        #     return api_response(
        #         status_code=400,
        #         message="Donatur not found, please fill the donatur data first",
        #         data={}
        #     )
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
