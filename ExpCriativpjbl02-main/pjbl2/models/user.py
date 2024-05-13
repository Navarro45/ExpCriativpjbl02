import flask_login

users = {
"adm": "adm1",
"user1":"1234",
"user2":"12345"
}

first_login_adm = True


class User(flask_login.UserMixin):
    pass

def get_users():
    global users
    return users

def add_user(user, password):
    users[user] = password
    return users

def remove_user(user):
    users.pop(user)
    return users

