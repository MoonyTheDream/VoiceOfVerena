import sqlite3

from flask import Flask, render_template
from markupsafe import escape

db_connection = sqlite3.connect('db/verenawisdom.sqlite3')
db_cursor = db_connection.cursor()

db_cursor.execute("SELECT * FROM profesje")
profesje = db_cursor.fetchall()

app = Flask(__name__)

@app.route("/")
@app.route("/<person>")
def hello(person=None):
    return render_template('testhtml.html', person=person)

@app.route("/postaci", methods=["GET", "POST"])
def character_sheets():
    from flask import request
    result = None
    race = None
    profession = None
    if request.method == "POST":
        race = request.form.get("race")
        profession = request.form.get("profession")
        # Prosty framework logiki - tu można rozbudować
        if race:
            result = f"Wybrana rasa: {race.capitalize()}"
            if profession:
                result += f", profesja: {profession.capitalize()}"
        else:
            result = "Nie wybrano rasy."
    return render_template('postaci.html', result=result, race=race, profession=profession, debug=profesje)

@app.route("/ceny")
def rules():
    return render_template('ceny.html')

@app.route("/kontakt")
def contact():
    return render_template('kontakt.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')