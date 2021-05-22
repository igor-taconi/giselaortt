from typing import NoReturn

from flask import Blueprint, Flask

from app.config import static_folder, template_folder
from app.ext.site.views import about, blog, index, login, store

bp = Blueprint(
    "ui",
    __name__,
    template_folder=template_folder,
    static_folder=static_folder,
)

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/store", view_func=store)
bp.add_url_rule("/login", view_func=login, endpoint="login")
bp.add_url_rule("/blog", view_func=blog)
bp.add_url_rule("/about", view_func=about)


def init_app(app: Flask) -> NoReturn:
    app.register_blueprint(bp)
