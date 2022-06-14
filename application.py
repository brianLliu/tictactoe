from tempfile import mktemp
from flask import Flask, render_template, session, url_for, redirect
from tempfile import mkdtemp
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mktemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/game/<int:row>/<int:column>")
def play(row, column):
    turn = session["turn"]
    session["board"][row][column] = turn
    session["turn"] = "O" if turn =="X" else "X"

    return redirect(url_for('index'))
