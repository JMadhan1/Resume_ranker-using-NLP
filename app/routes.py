# app/routes.py

# Change this line:
# from .cv_processor import process_and_save_scores

# To this absolute import:
from app.cv_processor import process_and_save_scores

# The rest of your routes.py code follows here...
# For example:
from flask import Blueprint

# Define your Blueprint
routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/some_route')
def some_function():
    # Use process_and_save_scores as needed
    scores = process_and_save_scores()
    return {"scores": scores}
