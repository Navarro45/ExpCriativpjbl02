from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
<html>
    <head>
    <title>Minha Casa</title>
    </head>
    <body>
    <h2>Minha Casa</h2>
    <h3>Acesse o menu:</h3>
    <ul>
        <li><a href="/sensors">Listar Sensores</a></li>
        <li><a href="/actuators">Listar Atuadores</a></li>
        <li><a href="/bedroom">Quarto</a></li>
        <li><a href="/bathroom">Banheiro</a></li>
    </ul>
    </body>
</html>
"""

@app.route('/sensors')
def sensors():
    return """
<html>
    <head>
        <title>Listar sensores</title>
    </head>
    <body>
        <h2>Sensores</h2>
        <ul>
            <li><a href="/light-sensor">Sensor de Luminosidade</a></li>
            <li><a href="/humidity-sensor">Sensor de Umidade</a></li>
        </ul>
        <li><a href="/">Inicio</a></li>
    </body>
</html>
"""

@app.route('/actuators')
def actuators():
    return """
<html>
    <head>
      <title>Listar atuadores</title>
    </head>
    <body>
        <h2>Atuadores</h2>
        <ul>
            <li><a href="/switch">Interruptor</a></li>
            <li><a href="/smart-lamp">Lâmpada Inteligente</a></li>
        </ul>
        <li><a href="/">Inicio</a></li>
    </body>
</html>
"""

@app.route('/bedroom')
def bedroom():
    return """
<html>
    <head>
        <title>Quarto</title>
    </head>
    <body>
        <h2>Quarto</h2>
        <p>[Detalhes do quarto]</p>
        <li><a href="/">Inicio</a></li>
    </body>
</html>
"""

@app.route('/bathroom')
def bathroom():
    return """
<html>
    <head>
        <title>Banheiro</title>
    </head>
    <body>
        <h2>Banheiro</h2>
        <p>[Detalhes do banheiro]</p>
        <li><a href="/">Inicio</a></li>
    </body>
</html>
"""

@app.route('/light-sensor')
def light_sensor():
    return """
<html>
    <head>
        <title>Sensor de Luminosidade</title>
    </head>
    <body>
        <h2>Sensor de Luminosidade</h2>
        <p>Status: [Inserir status do sensor aqui]</p>
        <li><a href="/">Inicio</a></li>
    </body>
</html>
"""

@app.route('/humidity-sensor')
def humidity_sensor():
    return """
<html>
    <head>
        <title>Sensor de Umidade</title>
    </head>
    <body>
        <h2>Sensor de Umidade</h2>
        <p>Status: [Inserir status do sensor aqui]</p>
        <li><a href="/">Inicio</a></li>
    </body>
</html>
"""

@app.route('/switch')
def switch():
    return """
<html>
    <head>
        <title>Interruptor</title>
    </head>
    <body>
        <h2>Interruptor</h2>
        <p>[Estado do interruptor]</p>
        <li><a href="/">Inicio</a></li>
    </body>
</html>
"""

@app.route('/smart-lamp')
def smart_lamp():
    return """
<html>
    <head>
        <title>Lâmpada Inteligente</title>
    </head>
    <body>
        <h2>Lâmpada Inteligente</h2>
        <p>[Estado da lâmpada]</p>
        <li><a href="/">Inicio</a></li>
    </body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
