from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SelectField
from wtforms.validators import Required, EqualTo, InputRequired, Optional

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

digits_list = range(2, 10)
rules = {
"A1":"多退少补法 - 自左向右计算"
}
count_of_numbers = range(2, 10)
class SetupForm(FlaskForm):
    digits = SelectField(u"Select Digits", [Optional()], choices=[(f, f) for f in digits_list])
    rule = SelectField(u"Select Rule", [Optional()], choices=[(k + ":" + v, k + ":" + v) for k, v in rules.items()])
    count_of_numbers = SelectField(u"Select count of numbers", [Optional()], choices=[(k, k) for k in count_of_numbers])
    class Meta:
        csrf = False
