from flask import Blueprint, render_template, abort, request, current_app, session, jsonify
from jinja2 import TemplateNotFound
from api.utils import (load_json_file,
                            read_file,
                            reverse_dict,
                            show_help)
import json
from datetime import datetime
from models.persister import Rule
from controller.baseview import (
                                generate_numbers_for_addition,
                                add_, minus_, multiply_, divide_, setup_add
                                )
import time
from wtf_forms.forms import LoginForm, RegisterForm, SetupForm

bp_calc = Blueprint('calc_view', __name__, template_folder='templates') #, url_prefix="/weather")

start_time = time.time()

# @weather_view.before_request
# def connect_db():
#     weather_view.dbhelper = WeatherDB()

@bp_calc.route('/', methods=['GET'])
def home():
    login_form = LoginForm()
    register_form = RegisterForm()
    setup_form = SetupForm()
    # weather_form = WeatherForm()
    return render_template("index.html", login_form=login_form, register_form=register_form, setup_form=setup_form)

#@bp_calc.route('/<calc_type>/rule/1/count_of_numbers/2', defaults={"calc_type":"add", "rule_id":"1", "count_of_numbers":"2"}, methods=['POST'])
@bp_calc.route('/<calc_type>/rule/<rule_id>/count_of_numbers/<count_of_numbers>/digits/<digits>', methods=['POST'])
def add(calc_type, rule_id, digits, count_of_numbers):
    # generate{count_of_numbers} random numbers based on rule_id
    numbers_list = generate_numbers_for_addition(rule_id, int(count_of_numbers), int(digits))
    formula = suffix = expected_result = ""
    if calc_type == "add":
        suffix = "+ "
        expected_result = add_(*numbers_list)
    elif calc_type == "minus":
        suffix = "- "
        expected_result = minus_(*numbers_list)
    elif calc_type == "multiply":
        suffix = "* "
        expected_result = multiply_(*numbers_list)
    elif calc_type == "divide":
        suffix = "/ "
        expected_result = divide_(*numbers_list)
    for x in numbers_list:
        formula += f"{x} " + suffix
    print(formula, "------")
    print(expected_result)
    data = {'success':True, 'status': True , "formula": formula.rstrip(suffix), "expected_result":expected_result,
              'message': "", 'ContentType':'application/json'}
    print(data)
    return json.dumps(data)

@bp_calc.route('/<calc_type>/setup', methods=['POST'])
def setup(calc_type):
    setup_form = SetupForm()
    digits = setup_form.digits.data
    rules = setup_form.rule.data
    count_of_numbers = setup_form.count_of_numbers.data
    digits = setup_form.digits.data
    rule_id = rules.split(":")[0]
    rule_desc = rules.split(":")[1]
    last_updated_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("rule is: " + rule_desc)
    rule = Rule(calc_type, rule_id, rule_desc, digits, count_of_numbers, last_updated_on)
    setup_add(rule)
    data = {'success':True, 'status': True , "rule_id":rule_id, "rule_desc": rule_desc, "digits":digits,
            "count_of_numbers":count_of_numbers, "url":f"/{calc_type}/rule/{rule_id}/count_of_numbers/{count_of_numbers}",
            'message': "Saved", 'ContentType':'application/json'}
    print(data)
    return json.dumps(data)


# @calc_view.after_request
# def teardown_():
#     dbhelper.close_()
