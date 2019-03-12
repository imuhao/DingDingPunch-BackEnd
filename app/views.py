from flask import render_template,request,redirect,url_for,jsonify
from app import app
from app import photos
import os
from datetime import datetime

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/uploadFile',methods=[ 'POST'])
def upload_file():
    filename = photos.save(request.files['photo'])
    file_url = photos.url(filename)
    return file_url

@app.route('/photoList',methods=['GET'])
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

@app.route('/photoListJson',methods=['GET'])
def photo_list_json():
    photo_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    phone_name = []
    for photo in photo_list:
        timeFormat = photo.split('.')[0]
        time = datetime.strptime(timeFormat,"%Y-%m-%d-%H-%M-%S")
        phone_name.append("%s年%s月%s日%s时%s分%s秒 星期%s"%(time.year,time.month,time.day,time.hour,time.minute,time.second,time.isoweekday()))
    photo_list=photo_list+photo_list
    phone_name=phone_name+phone_name
    return jsonify({"name":phone_name,"photo":photo_list})

    