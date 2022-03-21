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

@app.route('/secret')
def render_secret():
    return '''<br><br><br><br><br> <p align="center"><iframe width="840" height="470" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&mute=1&controls=0"></iframe></p>
           <p align="center">░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄<br>
            ░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄<br>
            ░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█<br>
            ░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█<br>
            ░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█<br>
            █▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█<br>
            █▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█<br>
            ░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█<br>
            ░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█<br>
            ░░░█░░██░░▀█▄▄▄█▄▄█▄████░█<br>
            ░░░░█░░░▀▀▄░█░░░█░███████░█<br>
            ░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█<br>
            ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█<br>
            ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█<br>
            ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█</p>'''
