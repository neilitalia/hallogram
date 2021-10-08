from datetime import datetime
from models.db import db
from sqlalchemy.orm import joinedload


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    costume = db.Column(db.String(255), nullable=False)
    claps = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", cascade='all',
                           backref=db.backref('users', lazy=True))

    def __init__(self, content, costume, claps, user_id):
        self.content = content
        self.costume = costume
        self.claps = claps
        self.user_id = user_id

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
        query = Post.query.options(joinedload(
            'user')).all()
        response = []
        for item in query:
            response.append({**item.json(), "user": item.user.json()})
        return response

    @classmethod
    def find_by_id(cls, post_id):
        post = Post.query.filter_by(id=post_id).first()
        return post
