from flask import Flask, render_template, redirect, url_for ,request, json
from flask_mqtt import Mqtt
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



temperatura = 0
umidade = 0
fumaca = 0
alerta = ''

# Configuração MQTT
app.config['MQTT_BROKER_URL'] = 'www.mqtt-dashboard.com'
app.config['MQTT_USERNAME'] = 'user' 
app.config['MQTT_PASSWORD'] = '123456'
app.config['MQTT_KEEPALIVE'] = 60 
app.config['MQTT_TLS_ENABLED'] = False

# Definição dos tópicos
MQTT_TOPIC_TEMPERATURE = "Temperatura.topic"
MQTT_TOPIC_HUMIDITY = "Umidade.topic"
MQTT_TOPIC_FUMACA = "Fumaca.topic"
MQTT_TOPIC_SEND = "Receber.topic"

mqtt_client = Mqtt()
mqtt_client.init_app(app)

# Funções MQTT
@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
  if rc == 0:
    mqtt_client.subscribe(MQTT_TOPIC_TEMPERATURE)
    mqtt_client.subscribe(MQTT_TOPIC_HUMIDITY)
    mqtt_client.subscribe(MQTT_TOPIC_FUMACA)
    print("Conectado!")

@mqtt_client.on_message()
def handle_message(client, userdata, message):
  global temperatura, umidade, alerta, fumaca
  topic = message.topic
  content = json.loads(message.payload.decode())
  if topic == MQTT_TOPIC_TEMPERATURE:
    temperatura = int(content)
    if temperatura > 35:
      alerta = "Alerta! Temperatura muito alta"
      mqtt_client.publish(MQTT_TOPIC_SEND, alerta)
    else:
      alerta = ""
  if topic == MQTT_TOPIC_HUMIDITY:
    umidade = int(content)
    if umidade < 25:
      alerta = "Alerta! Umidade muito baixa"
      mqtt_client.publish(MQTT_TOPIC_SEND, alerta)
    else:
      alerta = ""
  if topic == MQTT_TOPIC_FUMACA:
    fumaca = float(content)
    if 0 < fumaca < 100:
      alerta = "Nivel de Fumaça Baixo"
    elif 100 < fumaca < 700:
      alerta = "Nivel de Fumaça Médio"
    else:
      alerta = "Nivel de Fumaça Alto"
  else:
    alerta = ""

@mqtt_client.on_disconnect()
def handle_disconnect():
  print("Desconectado do Broker!")

# Função para a Central de Monitoramento     
@app.route('/central')
def central():
  global temperatura, umidade, fumaca
  return render_template("central.html", temperatura=temperatura, umidade=umidade, fumaca=fumaca)

@app.route('/controle', methods=['GET', 'POST'])
def remoto():
  if request.method == 'POST':
    mensagem = request.form['texto']
    mqtt_client.publish(mensagem, mensagem)
  return render_template("comando_remoto.html")

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