from typing import NoReturn

from flask import Blueprint, Flask

from app.config import static_folder, template_folder
from app.ext.site.views import (
    about,
    contact,
    index,
    ilustrations,
    publications
)

bp = Blueprint(
    "ui",
    __name__,
    template_folder=template_folder,
    static_folder=static_folder,
)

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/contato", view_func=contact)
bp.add_url_rule("/publicacoes", view_func=publications)
bp.add_url_rule("/sobre", view_func=about)
bp.add_url_rule("/ilustracoes", view_func=ilustrations)


def init_app(app: Flask) -> NoReturn:
    app.register_blueprint(bp)
