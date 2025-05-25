# Taylor Swift | The Eras Tour: surprise song tracker
#### Video Demo:  https://youtu.be/RFA_Xfbe3kk
#### Description: Web app made using HTML, CSS, JavaScript, SQLite, Flask, Python and Jinja for tracking how many times Taylor Swift played what song in ‘Surprise Song Acoustic Section’ during her Taylor Swift | The Eras Tour. The user can find a song that the famous singer-songwriter has performed and with a click of a button increase its _plays_ value in the songs.db database. Songs are sorted by albums and the number of times they have been played so far, but it is possible to see all the released songs in Swift's discography and the number of times they have been played!


### Basic information:
- this is a CS50x 2024 final project
- **author:**  Kristijan Bilanović
    - **GitHub:** [KristijanBilanovic](https://github.com/KristijanBilanovic)
- **made in:**  Zagreb, Croatia (🇭🇷)
- [Bootstrap](https://getbootstrap.com/) was used for CSS styling of some HTML elements
- all assets used in this project (images) are for educational purposes **ONLY**
- **libraries used:**
    - Flask
    - cs50


## App structure
- furthure break down of this web app by its structure

### _app.py_
- this is the main file of the web app, it contains all the routs and logic behind server authentication of song titles
- each route has a GET and a POST method:
    - **GET** loads data from database _songs.db_ and sends it to HTML site as a list of dictionaries that contains all the information about songs from one particular album or from the singer's entire discography; it is then displayed in a table using Jinja syntax and formatted with a help of the Bootsrap
    - **POST** method is used to submit user’s request to increment the number of times particular song has been played
        - when submitted, user's request is checked by being compared to names stored in _songs.db_ database to ensure the user did not change value of any particular button; if the value is changed, an ERROR message with code 400 appears on user’s screen which has been implemeted in apology.html file as per below:

        <br></br>
        server-side authentication in  _app.py_:

        ``` Python
        songs = db.execute("SELECT * FROM songs WHERE album = ? ORDER BY plays DESC;", "Taylor Swift")
        button = request.form.get("button")
        title = ""

        for song in songs:
            if button == song["title"]:
                title = button
                break
        if not title:
            return render_template("apology.html")
        ```

        <br></br>
        HTML site in _apology.html_:
        ```HTML
        {% extends "layout.html" %}

        {% block main %}

        <div class = "apology_logo">
            <h1>😕 Sorry, smoething went wrong! 😕</h1>
        </div>

            <br><br><br><br>

            <div style = "text-align: center;">
                <p style = "font-size: 300%; font-family: Arial;">ERROR: 400</p>
            </div>

            <br><br>

            <div style = "text-align: center;">
                <p style = "font-size: 150%; font-family: Arial;">Please, try again!</p>
            </div>

            <br><br><br>

            <div style = "text-align: center;" class = "container-fluid">
                <img class="img-fluid" style = "border-radius: 5%;" src = "../static/imgs/confused.gif">
            </div>

            <br><br><br><br>



        {% endblock %}
        ```

        <br></br>
        - once verified as valid, user’s input is modified in such a way that all instances of  “ _‘_ ” characters are doubled in order to make sure that that particular character is escaped when executing a SQLite command:

        escaping apostrophe in SQLite using Python:
        ```Python
        button = button.replace("'", "''")
        ```

        <br></br>
        - the song requested by the user is selected from the _songs.db_ database and its _plays_ value is temporarely stored in a Python variable, it is then increased by one, afterwhich the _plays_ value of the requested song is updated in the _songs.db_ database and the web app returns a redirect to the same page as per below:

        ```Python
        command = str("SELECT plays FROM songs WHERE album = 'Fearless' AND title = '" + button + "';")
        song = db.execute(command)

        plays = int(song[0]["plays"])
        plays += 1

        command = "UPDATE songs SET plays = " + str(plays) + " WHERE album = 'Fearless' ANd title = '" + button + "';"
        db.execute(command)

        return redirect("/fearless")
        ```
<br></br>
### _songs.db_
- database of songs, albums and the number of times that each song has been played during the acoustic set of the tour
- this database is made in SQLite
- <ins>ABOUT COLUMNS:</ins>
    - *id*   field is an autoincrementing primary key
    - *title*   field is a TEXT NOT NULL column
    - *album*   field is a TEXT NOT NULL column
    - *plays*   field is an INT NOT NULL column whose value is 0 by default

<br></br>
**_songs.db_ talbe:**
| id | title | album | plays |
| -- | ----- | ----- | ----- |
| 1 | Our Song (Taylor’s Version) | Taylor Swift (Taylor’s Version) | 3 |
| ⋮ | ⋮ | ⋮ | ⋮ |
| 113 | You’re On Your Own, Kid | Midnights | 5 |
| ⋮ | ⋮ | ⋮ | ⋮ |

> 🗒️ NOTE: <br>
>       values in this table are just placeholders for user to get a better grasp of the database structure and are not meat to be used in app


<br></br>
### _static/_
- a directory that contains all the necessary assets such as the CSS styling and the images (which are stored in directionary _imgs/_ for organisation purposes)

<br></br>
### _templates/_
- stores HTML websites that are being displayed as front-end of this web app
