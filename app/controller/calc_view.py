from flask import Blueprint, render_template, abort, request, current_app, session, jsonify
from jinja2 import TemplateNotFound
from api.utils import (load_json_file,
                            read_file,
                            reverse_dict,
                            show_help)
import json
from controller.baseview import (
                                generate_numbers_for_addition,
                                add_,
                                )
import time
from wtf_forms.forms import LoginForm, RegisterForm

bp_calc = Blueprint('calc_view', __name__, template_folder='templates') #, url_prefix="/weather")

start_time = time.time()

# @weather_view.before_request
# def connect_db():
#     weather_view.dbhelper = WeatherDB()

@bp_calc.route('/', methods=['GET'])
def home():
    login_form = LoginForm()
    register_form = RegisterForm()
    # weather_form = WeatherForm()
    return render_template("index.html", login_form=login_form, register_form=register_form)

@bp_calc.route('/add/rule/1/count_of_numbers/2', defaults={"rule_id":"1", "count_of_numbers":"2"}, methods=['POST'])
@bp_calc.route('/add/rule/<int:rule_id>/count_of_numbers/<int:count_of_numbers>', methods=['POST'])
def add(rule_id, count_of_numbers):
    login_form = LoginForm()
    register_form = RegisterForm()
    # generate{count_of_numbers} random numbers based on rule_id
    numbers_list = generate_numbers_for_addition()
    expected_result = add_(*numbers_list)
    print(expected_result, "------")
    formula = ""
    for x in numbers_list:
        formula += f"{x} + "
    print(formula, "------")
    print(expected_result)
    data = {'success':True, 'status': True , "formula": formula.rstrip("+ "), "expected_result":expected_result,
              'message': "", 'ContentType':'application/json'}
    print(data)
    #return jsonify(data=data)
    return json.dumps(data)
#    return render_template("index.html", login_form=login_form, register_form=register_form, data = json.dumps(data))

# @calc_view.after_request
# def teardown_():
#     dbhelper.close_()
