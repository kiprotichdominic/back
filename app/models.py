from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key=True)
    username =db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True , nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    password =db.Column(db.String(60),nullable=False)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
  

  
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    posted_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(225), default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.relationship('Comment', backref='post', lazy=True)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.posted_date}')"
    

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    
    
        
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments

    
    def __repr__(self):
        return f"User('{self.date_posted}')"