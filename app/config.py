import os

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
)
# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.

basedir = os.path.abspath(os.path.dirname(__file__))
template_folder = os.path.join(basedir, "../resources", "templates")
static_folder = os.path.join(basedir, "../resources", "static")
