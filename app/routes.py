""" routes.py - Defines the routes to endpoints """

from gpiozero import LED
from flask import request, render_template
from app import APP, PINS

@APP.route('/')
def index():
    """ Renders the default index template """
    return render_template("index.html")


@APP.route('/api/socketon', methods=['GET'])
def socket_on():
    """ Turns on passed socket """
    socket = request.args.get('socket_num')

    try:
        PINS[socket].on()
        return get_statuses(), '200'
    except:
        return 'Bad Request', '400' 


@APP.route('/api/socketoff', methods=['GET'])
def socket_off():
    """ Turns off passed socket """
    socket = request.args.get('socket_num')

    try:
        PINS[socket].off()
        return get_statuses(), '200'
    except:
        return 'Bad Request', '400'


@APP.route('/api/socketstatus', methods=['GET'])
def socket_status():
    """ Returns the status of the passed socket """
    return get_statuses(), '200'


def get_statuses():
    """ Private function for getting socket statuses """
    pinValues = {}
    for key, val in PINS.items():
        pinValues[key] = bool(val.value)

    return pinValues