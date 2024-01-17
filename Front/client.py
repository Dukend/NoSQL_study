from flask import Flask, render_template, redirect, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def authorization():
    responce = ('', 204)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        spam = request.form.get('newsletter')
        print("---------------")
        print(email)
        print(password)
        print(spam)
        print("---------------")
        if email == 'user@xxx.com' and password == '1234':
            return redirect("/dashboard")
    return render_template('login.html', wrong_pass_or_mail=True)


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    text = ''
    if request.method == 'POST':
        quiery = request.form.get('q')
        print(quiery)
        request_url = "http://localhost:8000/main/message/search/body?string=" + quiery
        result = requests.get(request_url)
        if result.status_code != 200:
            text = "backend server error!"
        print(result.json()[0].keys())
        text = result.json()[0]['Body']
    return render_template('dashboard.html', text = text)

@app.route('/post', methods=['POST', 'GET'])
def post():
    result = True
    return render_template('post.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        fname = request.form.get('fname')
        sname = request.form.get('sname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if password1 == password2:
            return redirect("/dashboard")
    return render_template('registration.html', wrong_pass_or_mail=True)

@app.route('/error', methods=['POST', 'GET'])
def error():
    return render_template('undefined_page.html')


if __name__ == "__main__":
    app.run(debug=False, port = 8085)