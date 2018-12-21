""" __init__.py """
import os
import asyncio
import datetime
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

def start_loop(loop):
  asyncio.set_event_loop(loop)
  loop.run_forever()

def checkTimes(pin_timers):
  print(datetime.datetime.now().time())
  asyncio.sleep(5)

new_loop = asyncio.new_event_loop()
new_loop.call_soon(checkTimes, PIN_TIMERS)
t = Thread(target=start_loop, args=(new_loop,))
t.start()

