from flask import Blueprint, Response

# Blueprint for Admin App
# This App route url start with '/admin'
admin = Blueprint('Admin', __name__)


# App routes are created below
@admin.route('/dashboard', methods=["GET"])
def dashboard():
    return Response({'key': 'value'})
