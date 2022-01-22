
from flask import Flask ,request,redirect,render_template,session,url_for

app=Flask(__name__)
app.secret_key='key'

@app.route('/') 
def index():
    return render_template('index.html')
@app.route('/signin',methods=['POST'])
def signin():
    accout=request.form['accout']
    password=request.form['password']
  
    if  (password =='test')and(accout=='test') :
        session['status']="登入中"
        return redirect(url_for('member'))
    elif (accout =='')or(password==''):
        return redirect(url_for('error',message='請輸入帳號、密碼'))
    else:
        return redirect(url_for('error',message='帳號、或密碼輸入錯誤'))

@app.route('/member/')
def member():
    username = session.get('status')
    if  username:
        return render_template('member.html')
    else:
        return render_template('index.html')


@app.route('/error/')
def error():
    message=request.args.get('message')
    return render_template('error.html',data=message)

@app.route('/signout')
def logout():
    session.pop('status') 
    #刪除session中的值：也是類似字典。可以有三種方式刪除session中的值。 session.pop(key) del session[key] session.clear()
    return redirect(url_for('index'))
    

#啟動網站伺服器 可透過port參數指定埠號
if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)

