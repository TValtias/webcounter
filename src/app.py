from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set-value", methods=["POST"])
def set_value():
    value = request.form.get("value")
    if value is None:
        return "Arvo puuttuu", 400

    try:
        new_value = int(value)
    except ValueError:
        return "Arvon tulee olla kokonaisluku", 400

    cnt.set_value(new_value)
    return redirect("/")
