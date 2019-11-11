from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Required')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Required')
    ])
    confirm_password = PasswordField('Confirm password', validators=[
        DataRequired(message='Required'),
        EqualTo('password', message='Passwords must match')
    ])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Required')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Required')
    ])


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message='Required')
    ])
    body = TextAreaField('Post Content', validators=[
        DataRequired(message='Required')
    ])


class CommentForm(FlaskForm):
    body = StringField('Comment',validators=[
        DataRequired(message="it\'s called a comment ya know"),
        Length(150)
    ])

