from flask import Flask
from app import config
from app import jpushutils
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
app = Flask(__name__)

app.config['SECRET_KEY']='Smile'
app.config['UPLOADED_PHOTOS_DEST'] = "app/static/images"
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app) 

from app import views
from app import api

