from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template("home.html")

@app.route('/menu')
def render_menu():
    return render_template("menu.html")

@app.route('/contact')
def render_contact():
    return render_template("contact.html")
