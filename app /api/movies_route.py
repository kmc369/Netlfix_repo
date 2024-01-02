from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Movie


movies_bp = Blueprint('movies',__name__)

@movies_bp.route("/get", method=["GET"])
def get_all_books():
    '''get all books'''
    movies = Movie.query.all()
    if not movies:
        return jsonify({"message": "No movies Found"})
    return [movie.to_dict() for movie in movies]

