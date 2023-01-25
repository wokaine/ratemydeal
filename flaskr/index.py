from flask import ( 
    Flask, url_for, Blueprint, flash, g, redirect, render_template, request, session 
)
import functools
from .db import *

# The original idea here was to scrape the Tesco website,
# however due to problems with getting requests I have gone
# for a hard coded approach by reading in options from a text
# file.

def getOptions():
    mains = []
    snacks = []
    drinks = []
    print("Importing mains...")
    with open('data/mains.txt', 'r') as file:
        mains = [line.rstrip() for line in file.readlines()]
    print("Done!")

    print("\nImporting snacks...")
    with open('data/snacks.txt', 'r') as file:
        snacks = [line.rstrip() for line in file.readlines()]
    print("Done!")

    print("\nImporting drinks...")
    with open('data/drinks.txt', 'r') as file:
        drinks = [line.rstrip() for line in file.readlines()]
    print("Done!")

    return mains, snacks, drinks

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def index():
    mains, snacks, drinks = getOptions()

    if request.method == 'POST':
        print("POST request received")
        print("Submit button...")

        print("Get main")
        main = request.form.get('main')
        print("get snack")
        snack = request.form.get('snack')
        print("get drink")
        drink = request.form.get('drink')

        uploadPost(main, snack, drink)
        print("Uploading deal")

        return redirect(url_for('posts_page'))
    elif request.method == 'GET':
        return render_template('index.html', mains=mains, snacks=snacks, drinks=drinks)