from flask import Blueprint, render_template, abort, request, current_app, session, url_for, redirect, jsonify, g
# from flask.ext.api import status
from jinja2 import TemplateNotFound
from wtf_forms.forms import LoginForm, RegisterForm
from controller.baseview import do_register, validate_user_login
from models.persister import User
from flask_bootstrap import Bootstrap

bp_login = Blueprint('login_view', __name__, template_folder='templates')

# To use global valirable "g"

history = {}
login_html = "login/login.html"


# @login_form_wtf.route("/login", methods=['GET'])
# @login_form_wtf.route('/', methods=['GET'])
# def login():
#     form = LoginForm()
#     if 'user' in session:
#         return jsonify(render_template("/weather/weather.html",
#                             form=WeatherForm(), username=session['user']))
#     else:
#         # return render_({ "template_file":login_html,
#         #              "form": form})
#         return render_template(login_html, form=form)

@bp_login.route('/register', methods=['GET'])
def register():
    form = RegisterForm()
    # return render_({    "template_file":"login/register.html",
    #                     "form": form})
    return render_template("login/register.html", form=form)


@bp_login.route('/login', methods=['POST'])
def login_view():
    login_form = LoginForm()
    print(login_form.username.data, "-----request data-----")
    # data = json.loads(request.data)
    username = login_form.username.data
    password = login_form.password.data
    # username = data.get('username')
    # password = data.get('password')
    user = User(username, password)
    print(username, password)
    if login_form.validate_on_submit():
        validated, message = validate_user_login(user)
        print("----", validated, message)
        if validated:
            session['user'] = username
            session['username'] = username
            session['user_id'] = message
            return jsonify({'username': username, 'success': True, 'status': '200',
                            'ContentType': 'application/json'})
        else:
            return jsonify({'success': False, 'status': '500', "message": {'message': message},
                            'ContentType': 'application/json'})  # , data={"username":username}))
    else:
        print(login_form.errors, ".........")
        # return jsonify(render_template("index.html", login_form=login_form, data={"message":login_form.errors}))
        return jsonify({'success': False, 'status': '500', "message": login_form.errors,
                        'ContentType': 'application/json'})  # , data={"username":username}))


@bp_login.route('/register', methods=['POST'])
def register_view():
    register_form = RegisterForm()
    login_form = LoginForm()
    username = register_form.username.data
    password = register_form.password.data
    confirm = register_form.confirm.data
    user = User(username, password)
    if register_form.validate_on_submit():
        result = do_register(user)
        print(result)
        print(result.get('message'), "---message---")
        if result.get('status'):
            return jsonify({'username': username, 'success': True, 'status': '200', "message": result.get('message'),
                            'ContentType': 'application/json'})  # , data={"username":username}))
        else:
            return jsonify({'username': username, 'success': False, 'status': '500', "message": result.get('message'),
                            'ContentType': 'application/json'})  # , data={"username":username}))

    else:
        print("validation message: ", register_form.errors)
        return jsonify({'success': False, 'status': '500', "message": register_form.errors,
                        'ContentType': 'application/json'})  # , data={"username":username}))
