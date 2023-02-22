import time
import threading
from flask import Flask
from plant_monitor import PlantMonitor

pm = PlantMonitor()

html = """
<!DOCTYPE html>
<meta http-equiv="refresh" content="5" >
<html>
    <head> 
        <title>My Plant</title> 
        <link rel="icon" href="https://www.raspberrypi.com/favicon.ico">
    </head>
    <body style="text-align: center; background-color: lightgrey; font-size: 50px">
        <h1>Raspberry OS Plant Monitor</h1>
        <h2>Wetness: {water} %</h2>
        <h2>Temperture: {temp} C</h2>
        <h2>Humidity: {humidity} %</h2>
    </body>
</html>
"""

app = Flask(__name__)

@app.route('/')
def index():
    
    #return render_template('index.html', plot_url='/static/plot.png')
    #return render_template('meter.py',t1.start())
    #return app
    #return 'Hello all'
    
    w = pm.get_wetness()
    t = pm.get_temp()
    h = pm.get_humidity()
    response = html.format(water=w, temp=t, humidity=h)
    return response, {'Content-Type': 'text/html'}
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    #app.run(debug=True)

