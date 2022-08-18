from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, validators
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.Length(min=8)])
    name = StringField('Name', validators=[validators.DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.Length(min=8)])
    submit = SubmitField('Login')

class CommentForm(FlaskForm):
    text = CKEditorField('Comments', validators=[DataRequired()])
    submit = SubmitField('Submit')