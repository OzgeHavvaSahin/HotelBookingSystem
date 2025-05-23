from flask import Blueprint
from flask_restx import Api

# Create the blueprint
api_blueprint = Blueprint('api', __name__)

# Initialize the Flask-RESTX API
api = Api(
    api_blueprint,
    version='1.0',
    title='Hotel Service API',
    description='Complete Hotel Management API with Swagger documentation',
    doc='/', 
)

from api.controllers.hotel_controller import hotel_ns

api.add_namespace(hotel_ns, path='/hotels')
