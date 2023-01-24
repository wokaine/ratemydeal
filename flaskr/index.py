from flask import ( 
    Flask, url_for, Blueprint, flash, g, redirect, render_template, request, session 
)
import functools

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')