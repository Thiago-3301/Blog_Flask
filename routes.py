from flask import request, render_template, redirect, url_for
from app import app, db
from models import Post

@app.route("/")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/post/add", methods=["POST"])
def add_post():
    try:
        form = request.form
        post = Post(title=form["title"], content=form["content"], author=form["author"])
        db.session.add(post)
        db.session.commit()
    except Exception as error:
        print("Error:", error)
    return redirect(url_for("home"))

@app.route("/post/<id>/del")
def delete_post(id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
    except Exception as error:
        print("Error:", error)
    return redirect(url_for("home"))

@app.route("/post/<id>/edit", methods=["GET", "POST"])
def edit_post(id):
    if request.method == "POST":
        try:
            post = Post.query.get(id)
            form = request.form
            post.title = form["title"]
            post.content = form["content"]
            post.author = form["author"]
            db.session.commit()
        except Exception as error:
            print("Error:", error)
        return redirect(url_for("home"))
    else:
        try:
            post = Post.query.get(id)
            return render_template("edit.html", post=post)
        except Exception as error:
            print("Error:", error)
        return redirect(url_for("home"))
