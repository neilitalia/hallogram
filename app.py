from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from resources import post, user

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/hallogram"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(user.Users, '/api/users')
api.add_resource(user.UserDetail, '/api/users/<int:user_id>')
api.add_resource(user.UserVerification,
                 '/api/users/verify')

api.add_resource(post.Posts, '/api/posts')
api.add_resource(post.PostDetail, '/api/posts/<int:post_id>')
api.add_resource(post.PostActions, '/api/posts/clap/<int:post_id>')

api.add_resource(post.PostImage, '/api/posts/image')

if __name__ == '__main__':
    app.run(debug=True)
