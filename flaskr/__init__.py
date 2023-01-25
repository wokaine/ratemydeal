from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

def create_app():
    print("Creating app...")

    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import index, posts
    app.register_blueprint(index.bp)
    app.register_blueprint(posts.bp)
    app.add_url_rule('/', endpoint='index')

    @app.route('/')
    def index_page():
        return index.index()

    @app.route('/posts')
    def posts_page():
        return posts.posts()

    return app