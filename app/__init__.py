from flask import Flask, render_template
from config import *

app = Flask(__name__)

app.config.from_object(Config)
