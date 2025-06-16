from flask import Flask, request, redirect, render_template, make_response

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    resp = make_response(redirect('/flag'))
    resp.set_cookie('username', username or '')
    resp.set_cookie('password', password or '')
    resp.set_cookie('admin', 'false')
    return resp

@app.route('/flag')
def flag():
    admin = request.cookies.get('admin')
    if admin == 'true':
        return render_template('flag.html')
    return "<h3>Access Denied. You are not admin.</h3>", 403

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    resp.set_cookie('admin', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)