""" routes.py - Defines the routes to endpoints """

from gpiozero import LED
from flask import request, render_template
from app import APP, PIN

@APP.route('/')
def index():
    """ Renders the default index template """
    return render_template("index.html")

@APP.route('/api/lighton', methods=['GET'])
def light_on():
    """ Turns on the light """
    PIN.on()
    return 'OK', '200'

@APP.route('/api/lightoff', methods=['GET'])
def light_off():
    """ Turns off the light """
    PIN.off()
    return 'OK', '200'

@APP.route('/api/lightstatus', methods=['GET'])
def light_status():
    return str(PIN.value), '200'
