from flask import Flask

# Blueprints
from server.web import web

def create_app():
    app = Flask(__name__)

    # Blueprints
    app.register_blueprint(web)

    return app
