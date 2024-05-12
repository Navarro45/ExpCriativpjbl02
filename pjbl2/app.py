from flask import Flask, render_template, redirect, url_for ,request
from login import login
import flask_login
import models.user
from user import user
from sensor import sensor
import models.sensor
import models.actuator
from actuator import actuator

atuadores = {'Servo': 122, 'Lâmpada': 1}

app = Flask(__name__)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(user, url_prefix='/')
app.register_blueprint(sensor, url_prefix='/')
app.register_blueprint(actuator, url_prefix='/')


app.secret_key = 'd54gdh543trg@!54gdh'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
users_ = models.user.get_users()
sensors_=models.sensor.get_sensors()
atuadores_=models.actuator.get_actuators()

@app.route('/')
def index():
    return render_template('login.html')

#callback user_loader carrega o usuário
# carrega usuário da seção
@login_manager.user_loader
def user_loader(user):
    users = users_
    if user not in users:
        return
    user_ = models.user.User()
    user_.id = user
    return user_

# carrega usuário do Flask request
@login_manager.request_loader
def request_loader(request):
    user = request.form.get('user')
    users = users_
    if user not in users:
        return
    user_ = models.user.User()
    user_.id = user
    return user_

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/sensors')
def sensors():
    return render_template("sensors.html",sensores=sensors_)

@app.route('/actuators')
def actuators():
    return render_template("actuators.html", atuadores=atuadores_)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)