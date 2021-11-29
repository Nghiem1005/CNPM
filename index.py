from flask import render_template, request, redirect
from my_app import app, utils
import hashlib


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/nhap_diem")
def diem():
    hocsinhs = utils.get_hocsinh("10A1")
    return render_template("NhapDiem.html", hocsinhs=hocsinhs)



@app.route('/api/insert_diem', methods=['post'])
def insertDiem():
    pass



if __name__ == '__main__':
    app.run(debug=True)