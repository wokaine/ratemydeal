from flask import request, jsonify
from flask_restful import Resource
from bson.objectid import ObjectId
from .db import db


class PostResource(Resource):
    def post(self):
        data = request.get_json()
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
        return jsonify({'message': 'Post added successfully!'}), 201

    def get_all(self):
        return list(db.posts.find({}))

    def get_from_id(self, post_id):
        return db.posts.find_one({"_id": ObjectId(post_id)})

    def post_comment(self, post_id):
        print("posting comment")
        data = request.get_json()
        print(post_id)
        post = db.posts.find_one({"_id": ObjectId(post_id)})
        if post:
            db.posts.update_one({"_id": ObjectId(post_id)}, {'$push': {'comments': data}})
            return jsonify({"message": "Comment sent successfully"}), 200
        return jsonify({"message": "Post not found"}), 404

    """ def like_post(self, post_id):
        post = db.posts.find_one({"_id": ObjectId(post_id)})
        if post:
            post["likes"] += 1
            db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": post})
            return jsonify({"message": "Post liked successfully"}), 200
        return jsonify({"message": "Post not found"}), 404
    
    def dislike_post(self, post_id):
        post = db.posts.find_one({"_id": ObjectId(post_id)})
        if post:
            post["dislikes"] += 1
            db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": post})
            return jsonify({"message": "Post disliked successfully"}), 200
        return jsonify({"message": "Post not found"}), 404 """

