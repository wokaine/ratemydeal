from flask import ( 
    Flask, url_for, Blueprint, redirect, render_template, 
)
import functools
from .db import *
from .post_resource import PostResource

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/posts', methods=('GET', 'POST'))
def posts():
    post_resource = PostResource()
    posts = post_resource.get_all()
    return render_template('posts.html', posts=posts)