import os
import logging
from flask import Flask
from routes import register_routes
from database import db, run_migrations

def create_initialized_flask_app():
    app = Flask(__name__, static_folder='static')

    # Set Flask secret key
    app.config['SECRET_KEY'] = 'supersecretflaskskey'

    # Initialize database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    db.init_app(app)

    # Run migrations
    run_migrations(app)

    register_routes(app)

    return app