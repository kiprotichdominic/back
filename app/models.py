from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, login_manager, app
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model,UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    username =db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True , nullable=False)
    password =db.Column(db.String(60),nullable=False)
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    posted_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(225), default='default.jpg')
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.posted_date}')"