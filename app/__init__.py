""" __init__.py """
import os
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

PIN = LED(4)

from app import routes