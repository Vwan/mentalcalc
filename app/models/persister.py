import sqlite3
import os
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from init import db

class UserRule(db.Model):
    __tablename__ = 'user_rules'
    id = db.Column(db.Integer, primary_key=True)
    calc_type = db.Column(db.String(80))
    rule_id = db.Column(db.String(120))
    rule_desc = db.Column(db.String(120))
    digits = db.Column(db.String(120))
    count_of_numbers = db.Column(db.String(120))
    last_updated_on = db.Column(db.String(120))
    user_id = db.Column(db.String(120))

    def __init__(self, calc_type, rule_id, rule_desc, digits, count_of_numbers, last_updated_on, user_id):
        self.calc_type = calc_type
        self.rule_id = rule_id
        self.rule_desc = rule_desc
        self.digits = digits
        self.count_of_numbers = count_of_numbers
        self.last_updated_on = last_updated_on
        self.user_id = user_id

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Rule(db.Model):
    __tablename__ = 'rules'
    id = db.Column(db.Integer, primary_key=True)
    calc_type = db.Column(db.String(80))
    rule_id = db.Column(db.String(120))
    rule_desc = db.Column(db.String(120))
    rule_summary = db.Column(db.String(120))

    def __init__(self, calc_type, rule_id, rule_summary, rule_desc):
        self.calc_type = calc_type
        self.rule_id = rule_id
        self.rule_desc = rule_desc
        self.rule_summary = rule_summary

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def as_dict(self):
       return {col.name: getattr(self, col.name) for col in self.__table__.columns}


db.drop_all()
db.create_all()
for calc_type in ["add", "minus"]:
    db.session.add(Rule(calc_type, "A1", "多退少补法 - 自左向右计算", "\
    例子: 58 + 65 =<p>\
    1. 5 + 6 = 11,<p> \
    2. 8 + 5 = 13， 因为大于10， 所以前面的 11 加 1，得 12，再取 13 的个位数 3，<p>\
    结果是 123<p>\
    "))
for calc_type in ["multiply", "divide"]:
    db.session.add(Rule(calc_type, "M1", "两位数 * 一位数", "\
    例子: 58 * 7 =<p>\
    1. 50 * 7 = 350, <p>\
    2. 8 * 7 = 56， <p>\
    3. 350 + 56, 从左向右计算，多退少补，得 406<p>\
    结果是 406<p>\
    "))
    db.session.add(Rule(calc_type, "M2", "两位数 * 两位数", """<p>
    例子: 58 * 17 =<p>
    1. 50 * 10 = 500, <p>
    2. 8 * 17 = 8 * 10 + 8 * 7 = 136， <p>
    3. 500 + 136, 从左向右计算，多退少补，得 35<p>
    结果是 636<p>
    """))
    db.session.commit()