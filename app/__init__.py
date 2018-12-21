""" __init__.py """
import os
import datetime
import time
from threading import Thread
from flask import Flask
from gpiozero import LED

class CustomFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))

APP = CustomFlask(__name__, 
          static_folder="./static",
          template_folder="./template")

PINS = {}
PINS['1'] = LED(3)
PINS['2'] = LED(4)

PINS['1'].off()
PINS['2'].off()

PIN_TIMERS = {}
PIN_TIMERS['1'] = { 'start': -1, 'end': -1}
PIN_TIMERS['2'] = { 'start': -1, 'end': -1}

from app import routes

@APP.before_first_request
def activateTimer():
  def checkTimes():
    while True:
      print(datetime.datetime.now().time())
      time.sleep(5)

  thread = threading.Thread(target=checkTimes)
  thread.start()
