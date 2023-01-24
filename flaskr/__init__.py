from flask import Flask, render_template
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import index
    app.register_blueprint(index.bp)

    @app.route('/')
    def index():
        return index.index()


    return app

if __name__ == '__main__':
    app = create_app
    app.run()