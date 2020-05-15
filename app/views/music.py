from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db
from app.models.Music import Music

music_pages = Blueprint('music', __name__, template_folder='templates')


@music_pages.route('/register', methods={'GET', 'POST'})
def register():
    if request.method == "POST":
        music = Music()
        music.title  = request.form['title']
        music.lyrics = request.form['lyrics']
        music.singer = request.form['singer']
        music.year   = request.form['year']
        db.session.add(music)
        db.session.commit()
        return redirect(url_for('core.index'))
    return render_template('music/register.html')

@music_pages.route('/<int:id>')
def music(id):
    music = Music.query.filter_by(id=id).first_or_404()
    return render_template('music/music.html', music=music)

@music_pages.route('/delete/<int:id>')
def delete(id):
    music = Music.query.filter_by(id=id).first_or_404()
    db.session.delete(music)
    db.session.commit()
    return redirect(url_for('core.index'))

@music_pages.route('/update/<int:id>', methods={'GET', 'POST'})
def update(id):
    if request.method == "POST":
        music = Music.query.filter_by(id=id).first_or_404()
        music.title  = request.form['title']
        music.lyrics = request.form['lyrics']
        music.singer = request.form['singer']
        music.year   = request.form['year']
        db.session.commit()
        return redirect(url_for('music.music', id=id))
    music = Music.query.filter_by(id=id).first_or_404()
    return render_template('music/update.html', music=music)
