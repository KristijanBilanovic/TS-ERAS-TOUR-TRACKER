import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///songs.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/debut", methods=["GET", "POST"])
def debut():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Taylor Swift")
        return render_template("debut.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Taylor Swift")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            num = int(button.rfind("'"))
            button = button[ : num] + "'" + button[num : ]
            command = str("SELECT plays FROM songs WHERE album = 'Taylor Swift' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'Taylor Swift' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/debut")

@app.route("/fearless", methods=["GET", "POST"])
def fearless():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Fearless")
        return render_template("fearless.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Fearless")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'Fearless' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'Fearless' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/fearless")

@app.route("/speaknow", methods=["GET", "POST"])
def speaknow():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Speak Now")
        return render_template("speaknow.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Speak Now")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'Speak Now' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'Speak Now' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/speaknow")


@app.route("/red", methods=["GET", "POST"])
def red():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "RED")
        return render_template("red.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "RED")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'RED' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'RED' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/red")

@app.route("/1989", methods=["GET", "POST"])
def album_1989():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "1989")
        return render_template("1989.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "1989")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = '1989' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = '1989' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/1989")

@app.route("/reputation", methods=["GET", "POST"])
def reputation():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "reputation")
        return render_template("reputation.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "reputation")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'reputation' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'reputation' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/reputation")

@app.route("/lover", methods=["GET", "POST"])
def lover():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Lover")
        return render_template("lover.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Lover")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'Lover' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'Lover' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/lover")

@app.route("/folklore", methods=["GET", "POST"])
def folklore():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "folklore")
        return render_template("folklore.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "folklore")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'folklore' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'folklore' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/folklore")

@app.route("/evermore", methods=["GET", "POST"])
def evermore():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "evermore")
        return render_template("evermore.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "evermore")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'evermore' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'evermore' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/evermore")

@app.route("/midnights", methods=["GET", "POST"])
def midnights():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Midnights")
        return render_template("midnights.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Midnights")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'Midnights' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'Midnights' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/midnights")

@app.route("/ttpd", methods=["GET", "POST"])
def ttpd():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "The Tortured Poets Department")
        return render_template("ttpd.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "The Tortured Poets Department")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'The Tortured Poets Department' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'The Tortured Poets Department' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/ttpd")

@app.route("/others", methods=["GET", "POST"])
def others():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Others")
        return render_template("others.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Others")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE album = 'Others' AND title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'Others' ANd title = '" + button + "';"
            db.execute(command)
            return redirect("/others")

@app.route("/eras", methods=["GET", "POST"])
def eras():
    if request.method == "GET":
        songs = db.execute("SELECT * FROM songs ORDER BY plays DESC;")
        return render_template("eras.html", songs = songs)

    if request.method == "POST":
        songs = db.execute("SELECT * FROM songs ORDER BY plays DESC;")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")

        else:
            button = button.replace("'", "''")
            command = str("SELECT plays FROM songs WHERE title = '" + button + "';")
            song = db.execute(command)
            plays = int(song[0]["plays"])
            plays += 1
            command = "UPDATE songs SET plays = " + str(plays) + " WHERE title = '" + button + "';"
            db.execute(command)
            return redirect("/eras")
