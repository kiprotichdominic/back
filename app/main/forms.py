from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, TextField, SelectField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


    
class CommentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit')