from flask import Flask
from app import config
from app import jpushutils
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from pymongo import MongoClient

app = Flask(__name__)

app.config['SECRET_KEY']='Smile'
app.config['UPLOADED_PHOTOS_DEST'] = "app/static/images"

# Photo Upload
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app) 

# MongoDB
client  = MongoClient("mongodb://smile:74521.@31.40.214.203/admin")
db = client.admin

from app import views
from app import api

