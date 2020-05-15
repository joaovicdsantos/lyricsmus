from . import db


class Music(db.Model):
    __tablename__ = "music"

    # Columns
    id     = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(84), nullable=False)
    lyrics = db.Column(db.Text, nullable=False)
    singer = db.Column(db.String(84), nullable=False)
    year   = db.Column(db.String(4), nullable=False)

    # Functions
    def __str__(self):
        return self.title
