from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User


movies_bp = Blueprint('movies',__name__)

