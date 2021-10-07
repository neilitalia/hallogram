from datetime import datetime
from models.db import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    costume = db.Column(db.String(255), nullable=False)
    claps = db.Column(db.Integer)

    def __init__(self, content, costume, claps):
        self.content = content
        self.costume = costume
        self.claps = claps

    def json(self):
        return {
            "id": self.id,
            "content": self.content,
            "costume": self.costume,
            "claps": self.claps,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        posts = Post.query.all()
        return [p.json() for p in posts]

    @classmethod
    def find_by_id(cls, town_id):
        post = Post.query.filter_by(id=town_id).first()
        return post
