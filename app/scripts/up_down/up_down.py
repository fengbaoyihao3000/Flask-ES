import os
import time

from flask import Flask, send_from_directory, jsonify, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "wocao"

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])

# 文件名是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download():
    try:
        dirpath = app.config['UPLOAD_FOLDER'] # os.path.join(app.root_path, 'static.download')
        return send_from_directory(dirpath,filename="1576669112.jpg", as_attachment=True)
    except Exception as e:
        print("download file error:", e)
        return jsonify(detail=str(e)), 422


@app.route('/upload', methods=['POST'])
def up_photo():
    file_dir = app.config['UPLOAD_FOLDER']
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # 文件夹不存在就创建
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    filename = secure_filename(f.filename)

    if f and allowed_file(filename):
        fname = f.filename
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 修改文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录

        return jsonify({"errno": 0, "errmsg": "上传成功"})
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})

if __name__ == '__main__':
    app.run()