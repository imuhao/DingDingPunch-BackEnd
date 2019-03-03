from flask import Flask
from app import config
from app import jpushutils

app = Flask(__name__)

from app import views
from app import api

