from flask import Flask , render_template,request,redirect,url_for,make_response

app= Flask(__name__)

app.secret_key = 'your_security_key' 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST'])
def setcookie():
    if request.method=='POST':
        user = request.form['username']
        resp = make_response(redirect(url_for('getcookie')))
        resp.set_cookie('username',user)
        return resp


@app.route('/getcookie')
def getcookie():
    username= request.cookies.get('username')
    return f'<h1>Welcome {username}!</h1>'


if __name__ == '__main__':
    app.run(debug=True)