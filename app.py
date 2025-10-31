from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/<person>")
def hello(person=None):
    return render_template('testhtml.html', person=person)

@app.route("/postaci")
def character_sheets():
    return render_template('postaci.html')

@app.route("/ceny")
def rules():
    return render_template('ceny.html')

@app.route("/kontakt")
def contact():
    return render_template('kontakt.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')