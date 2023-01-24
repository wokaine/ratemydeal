from flask import ( 
    Flask, url_for, Blueprint, flash, g, redirect, render_template, request, session 
)
import functools

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/posts', methods=('GET', 'POST'))
def posts():
    return render_template('posts.html')