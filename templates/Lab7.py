from flask import Flask, render_template, redirect, url_for
import datetime
import sys
if sys.version_info < (3,0):  # nghĩa là đây là cho phiên bản Python 2.x
    reload(sys)
    sys.setdefaultencoding('utf-8')

homnai = datetime.date.today()
homnay = datetime.date.today()

app = Flask(__name__,  static_folder = "D:\\Van_Lang\\bai1\\templates\\thumuchinh\\")

@app.route('/w')
def vidu_urlfor():
    return redirect(url_for('xuat_ra_web_mau'))  # <--- tên của def, không phải tên của route!

@app.route('/web')
def xuat_ra_web_mau():
    global homnai   # <--- biến ở bên ngoài
    homnay = 10     #  <--- biến này ở hàm, không liên quan đến biến bên ngoài
    ngay = str(homnai.day)
    thang = str(homnai.month)
    nam = str(homnai.year)
    ngaythangnam = ngay + "/" + thang + "/" + nam
    gido = 'gì đó'
    danhsach = ['Python nc', 'Lập trình web', 'CSDL']
    
    languages = [ {'STT':1, 'ten': "Python"}, {'STT':2, 'ten': "Java"} , {'STT':3, 'ten': "C++"}]
    languages.append({'STT':4, 'ten': ".NET" })
    languages.append({'STT':5, 'ten': "Matlab" })
    
    return render_template('abc.html',  ngaythang = ngaythangnam,
                           dsmon = danhsach,
                           nnlt = languages)


@app.route("/")   # <-- khai báo trang chủ  /
def trangchu():
    ketqua = '<b> Xin chào! </b>'
    return (ketqua)  # <--- chuỗi trong này là chuỗi html


@app.route("/sv/<tensv>")  # làm trang: localhost:5050/sv/NguyenVanA
def sinhvien(tensv):  
    global homnai
    namhoc = homnai.year
    hello1 = "Xin chào sinh viên khóa " + str(namhoc)
    hello2 = "Xin chào tháng " + str(homnai.month)
    
    hello3 = ""
    hovaten = str(tensv)
    if len(hovaten) > 0:
        hello3 = "Xin chào bạn " + hovaten
    
    hello = hello1 + " <p> " + hello2 + " <br> " + hello3
    return (hello)


# Hàm main:
if __name__ == "__main__":
    app.run(port = 5050)    # cổng mặc định là 5000
