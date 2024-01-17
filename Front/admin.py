from flask import Flask, render_template, redirect, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def authorization():
    responce = ('', 204)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'admin@xxx.com' and password == '1234':
            return redirect("/admin")
    return render_template('login.html', wrong_pass_or_mail=True)

@app.route('/error', methods=['POST', 'GET'])
def error():
    return render_template('undefined_page.html')

@app.route('/admin', methods=['POST', 'GET'])
def admin_panel():
    return render_template('admin_panel.html')


if __name__ == "__main__":
    app.run(debug=False, port = 8086)