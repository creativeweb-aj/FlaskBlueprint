import datetime
from App.extension import db
from werkzeug.security import check_password_hash, generate_password_hash


# Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_verify = db.Column(db.Boolean, default=False, nullable=False)
    created_on = db.Column(db.String, nullable=True)
    updated_on = db.Column(db.String, nullable=True)
    is_delete = db.Column(db.Boolean, default=False, nullable=True)

    def __repr__(self):
        return 'User : %r' % self.username


class EmailHandler(db.Model):
    __tablename__ = 'emailhandler'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=True)
    body = db.Column(db.String(200), nullable=True)
    uuid = db.Column(db.String(200), nullable=True)
    is_sent = db.Column(db.Boolean, default=False, nullable=False)
    is_expiry = db.Column(db.Boolean, default=False, nullable=False)
    is_verify = db.Column(db.Boolean, default=False, nullable=False)
    sent_on = db.Column(db.String, nullable=True)
    created_on = db.Column(db.String, nullable=True)
    updated_on = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'Email Handler : %r || %r' % self.id, self.user_id


# Create user method
def createUser(data):
    # Extract data from data
    firstName = data['firstName']
    lastName = data['lastName']
    userName = data['userName']
    email = data['email']
    password = data['password']

    # Generate password hash
    password = generate_password_hash(password)
    dateTime = datetime.datetime.utcnow()

    # Save data into model
    obj = User(first_name=firstName, last_name=lastName, username=userName, email=email, password=password,
               created_on=dateTime, updated_on=dateTime)
    db.session.add(obj)
    db.session.commit()
    return obj


# Login User
def loginUser(data):
    email = data['email']
    password = data['password']
    userObj = User.query.filter_by(email=email, is_active=True, is_verify=True, is_delete=False).first()
    if userObj is not None and check_password_hash(userObj.password, password):
        result = {
            "canLogin": True,
            "data": userObj.id
        }
    else:
        result = {
            "canLogin": False,
            "data": userObj.id
        }
    return result
