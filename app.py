from flask import Flask, request, redirect,url_for, render_template

app = Flask(__name__)

@app.route('/')     # route to the new/non-logged-in user homepage
def home():
    return render_template("index.html")

@app.route('/<name>') # route to the logged-in user homepage
def user_home(name):
    return render_template("user_home.html", content = name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555, debug=True)