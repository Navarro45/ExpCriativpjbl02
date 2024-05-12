import flask_login

sensores = {'T1':56, 'T2':25, 'T3':15}

class Sensor(flask_login.UserMixin):
    pass

def get_sensors():
    global sensores
    return sensores

def add_sensor(sensor, initial_value):
    sensores[sensor] = initial_value
    return sensores

def remove_sensor(sensor):
    sensores.pop(sensor)
    return sensores
