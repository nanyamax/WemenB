from flask import Blueprint, jsonify, url_for, request, redirect, session
from flask_cors import cross_origin
from app.models import User
from app.password import hash_password, check_password

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':
        json_data = request.json
        email = json_data.get("email")
        password = json_data.get("password")
        user = User.objects(email=email).first()
        if user:
            if check_password(user.password, password):
                data_to_return = {
                    "email": user.email,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "maritalStatus": user.maritalStatus,
                    "country": user.country,
                }
                response = jsonify(data_to_return)
                print(response)
                return  response,

            else:
                response = jsonify({"message": "Invalid email/password"})
                return response, 401
        else:
            response = jsonify({"message": "Invalid email/password"})
            return  response, 401
    else:
        response = jsonify({"message": "Invalid request"})
        return  response, 401


@auth.route('/logout')
def logout():
    # Manual session management
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    if request.method == 'POST':
        json_data = request.json
        email = json_data.get('email')
        first_name = json_data.get('firstName')
        last_name = json_data.get('lastName')
        password = json_data.get('password')
        password2 = json_data.get('password2')
        marital_status = json_data.get('maritalStatus')
        country = json_data.get('country')
        user = User.objects(email=email).first()
        if user:
            response = jsonify({"message": "Email already in use"})
            return  response, 401
        elif not email and len(email) < 5:
            response = jsonify({"message": "Invalid email address"})
            return  response, 401
        elif not first_name or len(first_name) < 2:
            response = jsonify({"message": "Invalid first name"})
            return  response, 401
        elif not last_name or len(last_name) < 2:
            response = jsonify({"message": "Invalid last name"})
            return  response, 401
        elif password != password2:
            print(password, password2)
            response = jsonify({"message": "Both password do not match"})
            return  response, 401
        else:
            hashed_password = hash_password(password)
            result = User(email=email, firstName=first_name, lastName=last_name, password=hashed_password,maritalStatus=marital_status, country=country).save()
            if result:
                data_to_post = {"firstName": result.firstName, "lastName": result.lastName, "email": result.email,
                                "maritalStatus": result.maritalStatus, "country": result.country}
                response = jsonify(data_to_post)
                return response
            else:
                response = jsonify({"message": "Could not create new user. Please try again"})
                return  response, 401
