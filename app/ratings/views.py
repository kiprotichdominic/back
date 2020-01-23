import os
from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint, current_app)
from flask_login import current_user, login_required, logout_user
from app import db, bcrypt
import secrets 
from PIL import Image
from app.models import Post, User, Comment
from app.ratings.forms import PostForm, CommentForm
from ..main import views

ratings = Blueprint('ratings', __name__)


def save_picture(form_image):
    randome_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_image.filename)
    picture_name = randome_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/featured_images', picture_name)
    output_size = (1000, 400)
    final_image = Image.open(form_image)
    final_image.thumbnail(output_size)
    final_image.save(picture_path)
    return picture_name
@ratings.route("/post/new", methods=['GET', 'POST'])
@login_required
def newpost():
    form = PostForm()
    if form.validate_on_submit():
        pic =None
        if form.image.data:
            picture_file = save_picture(form.image.data)
            final_pic = picture_file
            pic= final_pic
        post = Post(title=form.title.data, content=form.content.data, author=current_user, image=pic)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been published!', 'success')
        return redirect(url_for('main.home'))
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('newpost.html', title='New Post', form=form, legend='New Post', myposts=myposts)


@ratings.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.all()
    form = CommentForm()
    if form.validate_on_submit():
        content = Comment(content=form.content.data,author=current_user, post_id = post_id )
        db.session.add(content)
        db.session.commit()
        flash('Your comment has been posted!', 'success')
    return render_template("rate.html", form=form, post = post, comments=comments)