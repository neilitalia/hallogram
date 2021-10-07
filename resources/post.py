from models.db import db
from models.post import Post
from models.user import User
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Posts(Resource):
    def get(self):
        posts = Post.find_all()
        return posts

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        post = Post(**params)
        post.create()
        return post.json(), 201


class PostDetail(Resource):
    def get(self, post_id):
        post = Post.query.options(joinedload(
            'user')).filter_by(id=post_id).first()
        return {**post.json(), 'user': post.user.json()}

    def delete(self, post_id):
        post = Post.find_by_id(post_id)
        if not post:
            return {"msg": "Not found"}, 404
        db.session.delete(post)
        db.session.commit()
        return {"msg": "Post Deleted", "payload": post_id}


class PostActions(Resource):
    def put(self, post_id):
        post = Post.find_by_id(post_id)
        if not post:
            return {"msg": "Not found"}, 404
        # post.update({'claps': post.claps + 1})
        # setattr(post, claps, cl)
        post.claps += 1
        db.session.commit()
        return post.json()
