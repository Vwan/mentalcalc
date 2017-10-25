from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SelectField
from wtforms.validators import Required, EqualTo, InputRequired, Optional
from models.persister import Rule, db

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
# rules1 = {
# "A1":"多退少补法 - 自左向右计算"
# }


rules1 = Rule.query.filter_by(calc_type="add").all()
print("---rules1-----", rules1)
for k, v in enumerate(rules1):
    print(k, v.rule_id)
count_of_numbers = range(2, 10)
class SetupForm(FlaskForm):
    digits = SelectField(u"Select Digits", [Optional()], choices=[(f, f) for f in digits_list])
    rule = SelectField(u"Select Rule", [Optional()], choices=[(v.rule_id + ":" + v.rule_desc, v.rule_id + ":" + v.rule_summary) for k, v in enumerate(rules1)])
    count_of_numbers = SelectField(u"Select count of numbers", [Optional()], choices=[(k, k) for k in count_of_numbers])
    class Meta:
        csrf = False


rules2 = Rule.query.filter_by(calc_type="multiply").all()
class SetupMultiplyForm(FlaskForm):
    rule = SelectField(u"Select Rule", [Optional()], choices=[(v.rule_id + ":" + v.rule_desc, v.rule_id + ":" + v.rule_summary) for k, v in enumerate(rules2)])#, default="M1:两位数 * 一位数")
    # count_of_numbers = SelectField(u"count of numbers", render_kw={'disabled':''}, choices=[(f, f) for f in range(1,10)], default=2)
    # number1 = SelectField(u"Number 1", render_kw={'disabled':''}, choices=[(f, f) for f in range(1,10)], default=2)
    # number2 = SelectField(u"Number 2", render_kw={'disabled':''}, choices=[(f, f) for f in range(1,10)], default=1)
    # #
    # if rule == "M1:两位数*一位数":
    #     count_of_numbers.data = 2
    #     number1.data = 2
    #     number2.data = 1

    class Meta:
        csrf = False
