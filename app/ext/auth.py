from typing import Dict, NoReturn

from flask import Flask
from flask_simplelogin import SimpleLogin
from peewee import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User, db


def verify_login(user: Dict[str, str]) -> bool:
    """Valida o usuario e senha para efetuar o login."""
    username = user.get("username")
    password = user.get("password")
    email = user.get("email")

    if not username or not password or not email:
        return False

    try:
        existing_user = User.select().where(User.username == username).get()
        if check_password_hash(existing_user.password, password):
            return True

    except User.DoesNotExist:
        return False

    return False


def create_user(username, password, email):
    """Registra um novo usuario caso nao esteja cadastrado."""
    try:
        User.select().where(User.username == username).get()
        user = User.create(
            username=username, password=generate_password_hash(password), email=email
        )
        return user

    except IntegrityError:
        return {"erro": f"{username} ja esta cadastrado"}, 202


def init_app(app: Flask) -> NoReturn:
    SimpleLogin(app, login_checker=verify_login)
