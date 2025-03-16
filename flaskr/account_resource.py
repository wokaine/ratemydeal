from flask import request, jsonify, flash, redirect, url_for, session
from flask_restful import Resource
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from db import db


class AccountResource(Resource):
    def signup(self):
        data = request.get_json()
        username = data['enter_name']
        password = data['enter_password']
        existing_user = db.accounts.find_one({"username": username})
        if existing_user:
            print("Username already exists!")
            return jsonify({"exists": bool(existing_user)})
        else:
            account = {
                'username': username,
                'password': generate_password_hash(password),
                'liked_posts': [],
                'disliked_posts': []
            }
            db.accounts.insert_one(account)
            self.login()
            return jsonify({'message': 'Sign up successful!'}), 201

    def login(self):
        data = request.get_json()
        username = data['enter_name']
        password = data['enter_password']
        user = db.accounts.find_one({"username": username})

        if user and check_password_hash(user["password"], password):
            session["user"] = username
            flash("Login successful!", "success")
            return jsonify({'message': 'Login successful'}), 200
        
        return jsonify({'incorrect': not bool(user)})

