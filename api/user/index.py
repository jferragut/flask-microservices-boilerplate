# This is a demo for creating a user catchall endpoint that uses firestore
# To publish this, make sure you push your environment variables to your CI/CD

import os
from flask import Flask, request, jsonify, Response
from firebase_admin import credentials, firestore, initialize_app
from .model import User

# Initialize Flask App
app = Flask(__name__)

# Set an environment variables for GOOGLE_APPLICATION_CREDENTIALS in .env file to test locally
# to push to production on zeit, you will need to use the CLI to define and then expose it.
cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
# Initialize Firestore DB
default_app = initialize_app(cred)
db = firestore.client()
# if you are saving to a collection called users, you need to set this in a variable like so
user_ref = db.collection('users')

# the actual route is a catch-all, so you have to treat
# each request type as a conditional
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET','POST','PUT','DELETE'])
def catch_all(path):
    # Get User or Users
    # if you want a specific user pass an id parameter as a query string
    if(request.method=="GET"):
        try:
            # Check if ID or Username was passed to URL query
            # if so, return a single user
            user_id = request.args.get('id')
            user_name = request.args.get('username')

            if user_id:
                user_query = user_ref.where(u'id', u'==', user_id).stream()
                query_result = []
                for user in user_query:
                    query_result.append(
                        {
                            "doc_id": user.id,
                            "user": user.to_dict()
                        })
                return jsonify(query_result), 200

            if user_name:
                user_query = user_ref.where(u'username', u'==', user_name).stream()
                query_result = []
                for user in user_query:
                    query_result.append(
                        {
                            "doc_id": user.id,
                            "user": user.to_dict()
                        })
                return jsonify(query_result), 200

            # Otherwise, return all users
            else:
                all_users = [doc.to_dict() for doc in user_ref.stream()]
                return jsonify(all_users), 200
                
        except Exception as e:
            return "An exception of type {0} occurred. \nArguments: {1!r}".format(
                type(e).__name__, e.args)
    
    # Create User Record
    elif(request.method=="POST"):
        try:
            # set up the json object
            req = request.get_json()
            # define parameters from object
            user_id = req['user_id']
            username = req['username']
            first_name = req['first_name']
            last_name = req['last_name']
            friendly_name = req['friendly_name']
            password = req['password']
            password_hint = req['password_hint']
            # instantiate class for object to type check
            user = User(user_id=user_id, username=username, first_name=first_name,
                        last_name=last_name, friendly_name=friendly_name,
                        password=password, password_hint=password_hint)
            # no errors thrown, then write the user to firestore
            user_ref.document().set(user.to_dict())
            # return success
            return jsonify({"Success": True, "message": "The User has been successfully created."}), 200
        except KeyError as e:
            return f"The required property {e} is missing. Please include it in your request."
        except Exception as e:
            return "An exception of type {0} occurred. \nArguments: {1!r}".format(
                type(e).__name__, e.args)
        
    
    elif(request.method == "PUT"):
        try:
            id = request.json['id']
            user_ref.document(id).update(request.json)
            return jsonify({"Success": True, "message": "The User has been successfully updated."}), 200
        except Exception as e:
            return "An exception of type {0} occurred. \nArguments: {1!r}".format(
                type(e).__name__, e.args)
    
    elif(request.method == "DELETE"):
        try:
            # Check if ID or Username was passed to URL query
            user_id = request.args.get('id')
            user_name = request.args.get('username')

            if user_id:
                user_query = user_ref.where(u'id', u'==', user_id).stream()
                query_result = []
                for user in user_query:
                    query_result.append(
                        user.id)
                user_ref.document(query_result[0]).delete()
                return jsonify({"success": True, "message": "The User has been successfully deleted."}), 200

            if user_name:
                user_query = user_ref.where(
                    u'username', u'==', user_name).stream()
                query_result = []
                for user in user_query:
                    query_result.append(
                        user.id)
                user_ref.document(query_result[0]).delete()
                return jsonify({"success": True, "message":"The User has been successfully deleted."}), 200
        except Exception as e:
            return "An exception of type {0} occurred. \nArguments: {1!r}".format(
                type(e).__name__, e.args)

    else:
        return jsonify({"success": False, "message": "That request method isn't available on this endpoint."}), 405
