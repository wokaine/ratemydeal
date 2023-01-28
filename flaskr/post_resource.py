from flask import request, jsonify
from flask_restful import Resource
from .db import db


class PostResource(Resource):
    def post(self, data):
        data = request.get_json()
        print(data)
        post = {
            'main': data['main'],
            'snack': data['snack'],
            'drink': data['drink'],
            'submitted_by': data['enter_name'],
            'comments':[],
            'likes':0,
            'dislikes':0
        }
        db.posts.insert_one(post)
        print("Post added to DB (?)")
        return jsonify({'message': 'Post added successfully!'}), 201

    def get_all(self):
        return list(db.posts.find({}))
