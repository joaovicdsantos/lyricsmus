from flask import Blueprint, render_template
from app.models.Music import Music

core_pages = Blueprint('core', __name__, template_folder='templates')


@core_pages.route('/')
def index():
    music = Music.query.all()
    return render_template('core/index.html', music=music)
