from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label="username")
    email = StringField(label="Email")
    password1 = PasswordField(label="password1")
    password2 = PasswordField(label="password2")
    submit = SubmitField( label="CREATE ACCOUNT")
