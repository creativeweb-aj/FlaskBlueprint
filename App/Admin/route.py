from flask import Blueprint

# Blueprint for Admin App
# This App route url start with '/admin'
admin = Blueprint('Admin', __name__, url_prefix='/admin')


# App routes are created below
@admin.route('/dashboard')
def dashboard():
    return {'key': 'value'}
