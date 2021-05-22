from flask import flash, render_template, request


def index():
    name = "Olárrrrrrrrrrrrrrr"
    return render_template("index.html", name=name)


def store():
    return render_template("store.html")


def login():
    contact = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        contact = f"<Name {name}> {email}"
        flash("Logado com sucesso!", "success")

    return render_template("login.html", contact=contact)


def blog():
    return render_template("blog.html")


def about():
    return render_template("about.html")
