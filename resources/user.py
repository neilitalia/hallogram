from flask import request
from flask_restful import Resource
from models.user import User
from models.db import db
from sqlalchemy.orm import joinedload
from sqlalchemy import select


class Users(Resource):
    def get(self):
        users = User.find_all()
        return [u.json() for u in users]

    def post(self):
        data = request.get_json()
        user = User(**data)
        user.create()
        return user.json(), 201


class UserDetail(Resource):
    def delete(self, user_id):
        user = User.find_by_id(user_id)
        if not user:
            return {"msg": "user not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"msg": "User Deleted", "payload": user_id}

    def get(self, user_id):
        user = User.query.options(joinedload(
            'posts')).filter_by(id=user_id).first()
        posts = [p.json() for p in user.posts]
        return {**user.json(), 'posts': posts}


class UserVerification(Resource):
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['user_email'])
        if not user:
            return {"msg": "user not found"}, 404
        return user.json()
