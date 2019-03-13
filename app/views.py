from flask import render_template, request, redirect, url_for, jsonify
from app import app
from app import photos
import os
from datetime import datetime


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/uploadFile', methods=['POST'])
def upload_file():
    filename = photos.save(request.files['photo'])
    file_url = photos.url(filename)
    return file_url


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


@app.route('/photoListJson', methods=['GET'])
def photo_list_json():
    photo_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    phone_name = []
    for photo in photo_list:
        try:
            timeFormat = photo.split('.')[0]
            time = datetime.strptime(timeFormat, "%Y-%m-%d-%H-%M-%S")
            nowTime = datetime.now()
            num_to_ch=["一","二","三","四","五","六","日"]
            name = ""
            if nowTime.year != time.year:
                name = name+("%s年" % time.year)
            if(nowTime.year == time.year and nowTime.month != time.month):
                name = name+("%s月" % time.month)
            if(nowTime.year == time.year and nowTime.month == time.month and nowTime.day == time.day):
                name = name+("今天 ")
            if(nowTime.year == time.year and nowTime.month == time.month and nowTime.day != time.day):
                name = name+("%s日" % time.day)
            name = name+("%s时%s分%s秒 星期%s" %
                         (time.hour, time.minute, time.second, num_to_ch[time.weekday()]))
            phone_name.append(name)
        except:
            phone_name.append(photo)

    result = []
    for i in range(len(phone_name)):
        result.append({"time": phone_name[i], "photo": photo_list[i]})
    result.sort(key=lambda x: x['photo'], reverse=True)
    return jsonify(result)
