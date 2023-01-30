from flask import ( 
    Flask, url_for, Blueprint, redirect, render_template, jsonify
)
import functools
from .db import *
from .post_resource import PostResource

bp = Blueprint('posts', __name__, url_prefix='/posts')
post_resource = PostResource()

@bp.route('/posts', methods=('GET', 'POST'))
def posts():
    posts = post_resource.get_all()
    return render_template('posts.html', posts=posts)

@bp.route('/posts/view/<string:post_id>')
def view_post(post_id):
    post = post_resource.get_from_id(post_id)
    return render_template('viewpost.html', post=post)

@bp.route('/posts/view/<string:post_id>/submit_comment', methods=['PUT'])
def post_comment(post_id):
    post_resource.post_comment(post_id)
    return jsonify({"status": "success"}), 200


""" @bp.route('/posts/<string:post_id>/like', methods=['PUT'])
def like(post_id):
    post_resource = PostResource()
    return post_resource.like_post(post_id)

@bp.route('/posts/<string:post_id>/dislike', methods=['PUT'])
def dislike(post_id):
    post_resource = PostResource()
    return post_resource.dislike_post(post_id) """