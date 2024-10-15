import logging
from flask import render_template
from flask import current_app as app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_routes(app):
    @app.route("/")
    def home_route():
        return render_template("home.html")
    
    @app.route("/python")
    def python_route():
        return render_template("python.html")
    
    @app.route("/javascript")
    def javascript_route():
        return render_template("javascript.html")
    
    @app.route("/cpp")
    def cpp_route():
        return render_template("cpp.html")
    
    @app.route("/english")
    def english_route():
        return render_template("english.html")