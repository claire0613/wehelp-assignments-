from flask import Flask, request, redirect, render_template, session, url_for, jsonify
from datetime import timedelta
from database import db_insert, db_select, db_updateName
import os

# app = Flask(__name__)
app = Flask(__name__, static_folder="static", static_url_path="/static")

app.config['SECRET_KEY'] = os.urandom(16)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


@app.route('/')
def index():
    return render_template('index.html')

# 註冊


@app.route('/signup', methods=['POST'])
def signup():
    # 從前端接收資料
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    result = db_select(username=username)

    if (name == '') or (username == '') or (password == ''):
        return redirect(url_for('error', message='使用者姓名、帳號、密碼，皆不得為空白'))

    elif(result != None):
        return redirect(url_for('error', message='帳號已經被註冊'))
    else:
        db_insert(name=name, username=username, password=password)
        return redirect(url_for('index'))


# 登入
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if (username == '') or (password == ''):
        return redirect(url_for('error', message='帳號、密碼，皆不得為空白'))

    check_db = db_select(username=username, password=password)
    if check_db:
        name = check_db['name']
        session['name'] = name
        session['status'] = '登入中'
        session["username"] = username

        return redirect(url_for('member'))

    else:
        return redirect(url_for('error', message='帳號或密碼輸入錯誤'))

# 會員頁


@app.route('/member/')
def member():
    name = session.get('name')
    status = session.get('status')
    if status:
        return render_template('member.html', data=name)
    else:
        return redirect(url_for('index'))
 # 失敗畫面


@app.route('/error/')
def error():
    message = request.args.get('message')
    return render_template('error.html', data=message)

  # 登出


@app.route('/signout')
def logout():
    session.pop('name')
    session.pop('status')
    session.pop('username')
    # 刪除session中的值：也是類似字典。可以有三種方式刪除session中的值。 session.pop(key) del session[key] session.clear()
    return redirect(url_for('index'))


# 查詢會員資料(input帳號查會員姓名)
@app.route("/api/members", methods=["GET"])
def getUsername():
    if 'status' in session:
        username = request.args["username"]
        searchUsername = db_select(username=username)

        if searchUsername:
            data = {
                "id": searchUsername["id"],
                "name": searchUsername["name"],
                "username": searchUsername["username"]
            }
            return jsonify({"data": data})
        return jsonify({"data": 'null'})
    return redirect(url_for("index"))

# 修改會員姓名


@app.route("/api/member", methods=["GET", "POST"])
def updateData():
    if 'status' in session:
        data = request.get_json()  # {'name': inputed "newname"}
        name = data["name"]
        username = session["username"]
        db_updateName(name=name, username=username)
        aftUpdate = db_select(name=name, username=username)
        if name == aftUpdate['name']:
            return jsonify({"ok": True})
        return jsonify({"error": True})
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
