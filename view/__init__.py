from flask import Flask

from . import monitor

app = Flask(__name__)

app.register_blueprint(monitor.monitor)
#-----------------------------------------------------s