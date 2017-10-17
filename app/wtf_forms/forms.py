from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import Required, EqualTo, InputRequired

class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[Required(message="Username cannot be empty")])
    password = PasswordField("Password", validators=[Required(message="Password cannot be empty")])
    remember_me = BooleanField("Remember me?", default=False)

class RegisterForm(FlaskForm):
    username = StringField("User Name", [Required(message="Username cannot be empty")])
    password = PasswordField("Password",
                            [Required(message="Password cannot be empty"),
                            EqualTo('confirm', message="Password must match")])
    confirm = PasswordField("Repeat Password")

class WeatherForm(FlaskForm):
    city = StringField("City", validators=[InputRequired()])
    class Meta:
        csrf = False
