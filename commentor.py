from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://localhost/philippeterson'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    refcode = db.Column(db.String(255), unique=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_parent = db.ForeignKey('post.id')
    user = db.ForeignKey('user.id')
    approved = db.Column(db.Boolean)

    parent = db.ForeignKey('comment.id')
    text = db.Column(db.String(65535))
    date = db.Column(db.DateTime)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    hash = db.Column(db.String(100)) # should be plenty for bcrypt
    email = db.Column(db.String(255))
    join_date = db.Column(db.DateTime)
    verified = db.Column(db.Boolean)

if __name__ == '__main__':
   app.run()
