from models.db import db
from models.post import Post
from models.user import User
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload

class Posts(Resource):
  def get(self):
    books = Book.find_all()
    return books

def post(self):
    data = request.get_json()
    params = {}
    for k in data.keys():
        params[k] = data[k]
    book = Book(**params)
    book.create()
    return book.json(), 201