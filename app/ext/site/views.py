from flask import flash, render_template, request


def index():
    return render_template("index.html")


def contact():
    return render_template("contact.html")


def publications():
    return render_template("publications.html")


def about():
    return render_template("about.html")


def ilustrations():
    return render_template("ilustrations.html")
