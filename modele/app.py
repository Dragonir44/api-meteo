from flask import Flask, render_template, request
from Data.authors import authors
from Function.authors_util import get_author_by_id, get_author_by_name


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", authors=authors)

@app.route('/author/<id>')
def author(id):
    author = get_author_by_id(id)
    return render_template("author_details.html", author=author)