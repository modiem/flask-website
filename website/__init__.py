from flask import flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "noweotnbigusdlknt"
    return app