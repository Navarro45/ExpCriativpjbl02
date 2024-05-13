from flask import Blueprint, request, render_template, redirect, url_for

login = Blueprint("login",__name__, template_folder="templates")

user_name = []
user_password = []


@login.route('/register_user')
def register_user():
    return render_template("register_user.html")

@login.route('/add_user', methods=['GET','POST'])
def add_user():
    global user_name
    global user_password
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        user_name.append(user)
        user_password.append(password)
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
        user_name.append(user)
        user_password.append(password)
        
    return render_template("users.html", devices=user_name)

@login.route('/remove_user')
def remove_user():
    return render_template("remove_user.html",devices=user_name)

@login.route('/del_user', methods=['GET','POST'])
def del_user():
    global user_name
    global user_password
    if request.method == 'POST':
        print(request.form)
        user = request.form['user']
        for i in user_name:
            if user == user_name[i]:
                user_name.pop(i)
                user_password.pop(i)
            i += 1
    else:
        user = request.args.get('user', None)
        for i in user_name:
            if user == user_name[i]:
                user_name.pop(i)
                user_password.pop(i)
            i += 1
    return render_template("users.html", devices=user_name)