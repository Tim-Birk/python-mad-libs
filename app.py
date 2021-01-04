from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from storydata import pizza_party, the_queen, cooking_school

app = Flask(__name__)
app.config['SECRET_KEY'] = "specialsecret"

debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/story1")
def story1_form():
    return render_template("story-form.html", prompts=pizza_party.prompts, title = pizza_party.title, post_url="/story1")

@app.route("/story1", methods=["POST"])
def story1_show():
    story_text = pizza_party.generate(request.form)
    return render_template("story-display.html",story_text=story_text, title = pizza_party.title)

@app.route("/story2")
def story2_form():
    return render_template("story-form.html", prompts=the_queen.prompts, title = the_queen.title, post_url="/story2")

@app.route("/story2", methods=["POST"])
def story2_show():
    story_text = the_queen.generate(request.form)
    return render_template("story-display.html",story_text=story_text, title = the_queen.title)

@app.route("/story3")
def story3_form():
    return render_template("story-form.html", prompts=cooking_school.prompts, title = cooking_school.title, post_url="/story3")

@app.route("/story3", methods=["POST"])
def story3_show():
    story_text = cooking_school.generate(request.form)
    return render_template("story-display.html",story_text=story_text, title = cooking_school.title)