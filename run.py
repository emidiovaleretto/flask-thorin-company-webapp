import os
import json
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/api.json", "r") as api_file:
        data = json.load(api_file)
    return render_template("about.html", page_title="About", members=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/api.json", "r") as api_file:
        data = json.load(api_file)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash(f"Thanks {request.form['name']}, we have received your message!")
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ("IP", "0.0.0.0"),
        port=os.environ("PORT", "5000"),
        debug=False
    )