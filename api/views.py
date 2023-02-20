"""Hardcoded Flask views."""

from flask import Blueprint
#TODO: Needs blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')

@admin_bp.route("/")
def hello_world():
    return jsonify({'message':'Hello world!'})