from flask import Blueprint, request, render_template, redirect, url_for

login = Blueprint("login",__name__, template_folder="templates")

users = []


@login.route('/register_user')
def register_user():
    return render_template("register_user.html")

@login.route('/add_user', methods=['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
        users[user] = password
    return render_template("users.html", devices=users)

@login.route('/remove_user')
def remove_user():
    return render_template("remove_user.html",devices=users)

@login.route('/del_user', methods=['GET','POST'])
def del_user():
    global users
    if request.method == 'POST':
        print(request.form)
        user = request.form['user']
    else:
        user = request.args.get('user', None)
        users.pop(user)
    return render_template("users.html", devices=users)