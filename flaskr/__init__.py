from flask import Flask
from flask_restful import Api
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from post_resource import PostResource
from post_resource import post_resource
import os

def create_app():
    print("Creating app...")

    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import index, posts
    app.register_blueprint(index.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(post_resource)
    api.add_resource(PostResource, '/submit')
    app.add_url_rule('/', endpoint='index')

    @app.route('/')
    def index_page():
        return index.index()

    @app.route('/posts')
    def posts_page():
        return posts.posts()

    return app