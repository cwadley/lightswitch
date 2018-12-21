""" routes.py - Defines the routes to endpoints """

import json
from gpiozero import LED
from flask import request, render_template
from app import APP, PINS, PIN_TIMERS

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
        return json.dumps(get_statuses()), '200'
    except:
        return 'Bad Request', '400' 


@APP.route('/api/socketoff', methods=['GET'])
def socket_off():
    """ Turns off passed socket """
    socket = request.args.get('socket_num')

    try:
        PINS[socket].off()
        return json.dumps(get_statuses()), '200'
    except:
        return 'Bad Request', '400'


@APP.route('/api/settimer', methods=['GET'])
def set_timer():
    """ Sets the timer for the passed socket """
    socket = request.args.get('socket_num')
    startTime = request.args.get('start_time')
    endTime = request.args.get('end_time')

    try:
        PIN_TIMERS[socket]['start'] = startTime
        PIN_TIMERS[socket]['end'] = endTime
        return 'OK', '200'
    except:
        return 'Bad Request', '400'


@APP.route('/api/cleartimer', methods=['GET'])
def clear_timer():
    """ Clears the timer of the passed socket """
    socket = request.args.get('socket_num')

    try:
        PIN_TIMERS[socket]['start'] = -1
        PIN_TIMERS[socket]['end'] = -1
        return 'OK', '200'
    except:
        return 'Bad Request', '400'


@APP.route('/api/socketstatus', methods=['GET'])
def socket_status():
    """ Returns the status of the passed socket """
    return json.dumps(get_statuses()), '200'


def get_statuses():
    """ Private function for getting socket statuses """
    pinValues = {}
    for key, val in PINS.items():
        pinValues[key] = bool(val.value)

    return pinValues