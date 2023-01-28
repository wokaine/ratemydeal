from flask import Blueprint, request, jsonify, Flask
from flask_restful import  Resource
from db import db

post_resource = Blueprint('post_resource', __name__)

class PostResource(Resource):
    def post(self):
        data = request.get_json()
        post = {
            'main': data['main'],
            'snack': data['snack'],
            'drink': data['drink'],
            'comments':[],
            'likes':0,
            'dislikes':0
        }
        db.posts.insert_one(post)
        return jsonify({'message': 'Post added successfully!'}), 201
