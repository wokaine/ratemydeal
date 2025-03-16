from flask import Flask, render_template, jsonify, session
from flask_restful import Api
from account_resource import AccountResource
from post_resource import PostResource
import os
import sys
import secrets

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

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

def create_app():
    print("Creating app...")

    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.secret_key = secrets.token_hex(32)

    post_resource = PostResource()
    acc_resource = AccountResource()
    mains, snacks, drinks = getOptions()

    @app.route('/')
    def index_page():
        if "user" in session:
            username = session["user"]
        else:
            username = "Anonymous"
        return render_template('index.html', mains=mains, snacks=snacks, drinks=drinks, username=username)

    @app.route('/posts')
    def posts_page():
        posts = post_resource.get_all()
        return render_template('posts.html', posts=posts)

    @app.route('/submit', methods=['PUT'])
    def submit_deal():
        print("Submit button pressed")
        post_resource = PostResource()
        post_resource.post()
        return jsonify({"status": "success"}), 200

    """ @app.route('/posts/<post_id>/like', methods=['PUT'])
    def like_post(post_id):
        return post_resource.like_post(post_id)

    @app.route('/posts/<post_id>/dislike', methods=['PUT'])
    def dislike_post(post_id):
        return post_resource.dislike_post(post_id) """

    @app.route('/posts/view/<string:post_id>')
    def view_post_page(post_id):
        post = post_resource.get_from_id(post_id)
        return render_template('viewpost.html', post=post)

    @app.route('/posts/view/<string:post_id>/submit_comment', methods=['PUT'])
    def submit_comment(post_id):
        post_resource.post_comment(post_id)
        return jsonify({"status": "success"}), 200
    
    @app.route('/sign-up')
    def view_sign_up():
        return render_template('signup.html')  

    @app.route('/log-in')
    def view_log_in():
        return render_template('login.html')

    @app.route('/sign-up/submit', methods=['PUT'])
    def sign_up_submit():
        print("Submit button pressed")
        return acc_resource.signup()
    
    @app.route('/login/submit', methods=['PUT'])
    def login_submit():
        print("Submit button pressed")
        acc_res = AccountResource()
        return acc_res.login()
    
    @app.route('/login/submit')
    def logout():
        session.pop("user", None)
        return index_page()

    return app

app = create_app()
app.run()