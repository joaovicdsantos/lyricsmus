from flask import Flask
# Models
from .models import db, Music
# Views
from .views.core import core_pages
from .views.music import music_pages


def create_app():
    app = Flask(__name__)

    # Database
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Registering Views/Blueprints
    app.register_blueprint(core_pages)
    app.register_blueprint(music_pages, url_prefix="/music/")

    return app
