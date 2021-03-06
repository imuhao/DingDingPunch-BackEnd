from flask import render_template, request, redirect, url_for, jsonify
from app import app
from app import photos
import os
from datetime import datetime


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/photoList', methods=['GET'])
def manage_file():
    photo_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    return render_template('manage.html', files_list=photo_list)


@app.route('/open/<filename>')
def open_file(filename):
    file_url = photos.url(filename)
    return render_template('browser.html', file_url=file_url)


@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = photos.path(filename)
    os.remove(file_path)
    return redirect(url_for('manage_file'))

