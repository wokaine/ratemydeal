from flask import ( 
    Flask, url_for, Blueprint, flash, g, redirect, render_template, request, session 
)
import functools
from db import *

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/posts', methods=('GET', 'POST'))
def posts():
    posts = getPosts()
    return render_template('posts.html', posts=posts)