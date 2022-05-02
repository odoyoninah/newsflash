from flask import Blueprint
newsapp = Blueprint('newsapp', __name__)
from . import views

