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
            return True, existing_user.username
        else:
            return False, "User or Password incorrect, please retry"
    else:
        return False,  "user doesn't exist, please register first"

def do_register(user):
    # check if user exists
    existing_user = User.query.filter_by(username=user.username).first()
    print("---existing user---", existing_user)
    if existing_user:
        message = "User already exists, please login"
        status = False
    else:
        db.session.add(user)
        db.session.commit()
        message = "Registered successfully, please login"
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

def substract_(*args):
    return functools.reduce(operator.sub, args)

def multiply_(*args):
    return functools.reduce(operator.mul, args)

def divide_(*args):
    return functools.reduce(operator.truediv, args)

def generate_numbers_for_addition(rule_id=1, count_of_numbers=2, max_digits=2):
    numbers_list = []
    for i in range(count_of_numbers):
        number = randint(0, 10 ** max_digits)
        numbers_list.append(number)
    print(numbers_list)
    return numbers_list

if __name__ == "__main__":
    numbers_list = generate_numbers_for_addition()
    result_add = add_(*numbers_list)
    print(result_add)
    result_mul = multiply_(*numbers_list)
    print(result_mul)
    result_div = divide_(*numbers_list)
    print(result_div)
    result_sub = substract_(*numbers_list)
    print(result_sub)
