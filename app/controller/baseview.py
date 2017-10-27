from flask import request, current_app, render_template, session, jsonify
from jinja2 import TemplateNotFound
from flask_sqlalchemy import SQLAlchemy
from random import randint
import functools, operator
from models.persister import User, db

def validate_user_login(user):
    # check if user exists
    existing_user = User.query.filter_by(username=user.username).first()
    print("existing user is: ", existing_user)
    if existing_user:
        if existing_user.password == user.password:
            return True, existing_user.id
        else:
            return False, "用户名或密码不正确"
    else:
        return False,  "用户不存在，请先注册"

def do_register(user):
    # check if user exists
    existing_user = User.query.filter_by(username=user.username).first()
    print("---existing user---", existing_user)
    if existing_user:
        message = "用户已存在，请登录"
        status = False
    else:
        db.session.add(user)
        db.session.commit()
        message = "注册成功，请登录"
        status = True
    return {"message":message, "status":status}

def calc(func):
    def inner(*args):
        for arg in args:
            func(arg)
    return inner

#@calc
def add_(*args):
    return sum(args)

def minus_(*args):
    return functools.reduce(operator.sub, args)

def multiply_(*args):
    return functools.reduce(operator.mul, args)

def divide_(*args):
    return functools.reduce(operator.truediv, args)

def generate_numbers_for_addition(rule_id=1, count_of_numbers=2, max_digits=2):
    numbers_list = []
    print(count_of_numbers, "--------")
    for i in range(count_of_numbers):
        number = randint(10 * (max_digits -1), 10 ** max_digits)
        numbers_list.append(number)
    print(numbers_list, "-----numbers in list-----")
    return numbers_list

def generate_numbers_for_multiply(rule_id="M1"):
    numbers_list = []
    if rule_id == "M1":
        number1 = randint(11, 10 ** 2)
        number2 = randint(1,9)
        numbers_list.append(number1)
        numbers_list.append(number2)
    if rule_id == "M2":
        number1 = randint(11, 10 ** 2)
        number2 = randint(11, 10 ** 2)
        numbers_list.append(number1)
        numbers_list.append(number2)
    return numbers_list

def setup_add(rule):
    db.session.add(rule)
    db.session.commit()
    message = "保存成功"
    status = True
    return {"message":message, "status":status}

if __name__ == "__main__":
    numbers_list = generate_numbers_for_addition()
    result_add = add_(*numbers_list)
    print(result_add)
    result_mul = multiply_(*numbers_list)
    print(result_mul)
    result_div = divide_(*numbers_list)
    print(result_div)
    result_sub = minus_(*numbers_list)
    print(result_sub)
