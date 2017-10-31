from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SelectField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Optional
from models.persister import Rule, db
from flask import session


class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired(message="用户名不能为空")])
    password = PasswordField("密码", validators=[DataRequired(message="密码不能为空")])
    remember_me = BooleanField("记住密码?", default=False)


class RegisterForm(FlaskForm):
    username = StringField("用户名", [DataRequired(message="用户名不能为空")])
    password = PasswordField("密码",
                             [DataRequired(message="密码不能为空"),
                              EqualTo('confirm', message="密码不匹配")])
    confirm = PasswordField("确认密码")


digits_list = range(2, 10)
rules1 = Rule.query.filter_by(calc_type="add").all()
count_of_numbers = range(2, 10)


class SetupForm(FlaskForm):
    digits = SelectField(u"选择位数", [Optional()], choices=[(f, f) for f in digits_list])
    rule = SelectField(u"选择计算规则", [Optional()],
                       choices=[(v.rule_id + ":" + v.rule_desc, v.rule_id + ":" + v.rule_summary) for k, v in
                                enumerate(rules1)])
    count_of_numbers = SelectField(u"选择要计算的数字个数", [Optional()], choices=[(k, k) for k in count_of_numbers])

    class Meta:
        csrf = False


rules2 = Rule.query.filter_by(calc_type="multiply").all()


class SetupMultiplyForm(FlaskForm):
    rule = SelectField(u"选择计算规则", [Optional()],
                       choices=[(v.rule_id + ":" + v.rule_desc, v.rule_id + ":" + v.rule_summary) for k, v in
                                enumerate(rules2)])  # , default="M1:两位数 * 一位数")

    class Meta:
        csrf = False
