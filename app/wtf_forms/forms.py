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
rules1 = {
"A1":"多退少补法 - 自左向右计算"
}
count_of_numbers = range(2, 10)
class SetupForm(FlaskForm):
    digits = SelectField(u"Select Digits", [Optional()], choices=[(f, f) for f in digits_list])
    rule = SelectField(u"Select Rule", [Optional()], choices=[(k + ":" + v, k + ":" + v) for k, v in rules1.items()])
    count_of_numbers = SelectField(u"Select count of numbers", [Optional()], choices=[(k, k) for k in count_of_numbers])
    class Meta:
        csrf = False

rules2={
"M1":"两位数 * 一位数",
"M2":"两位数 * 两位数"
}
class SetupMultiplyForm(FlaskForm):
    rule = SelectField(u"Select Rule", [Optional()], choices=[(k + ":" + v, k + ":" + v) for k, v in rules2.items()], default="M1:两位数 * 一位数")
    count_of_numbers = SelectField(u"count of numbers", render_kw={'disabled':''}, choices=[(f, f) for f in range(1,10)], default=2)
    number1 = SelectField(u"Number 1", render_kw={'disabled':''}, choices=[(f, f) for f in range(1,10)], default=2)
    number2 = SelectField(u"Number 2", render_kw={'disabled':''}, choices=[(f, f) for f in range(1,10)], default=1)
    #
    # if rule == "M1:两位数*一位数":
    #     count_of_numbers.data = 2
    #     number1.data = 2
    #     number2.data = 1

    class Meta:
        csrf = False
