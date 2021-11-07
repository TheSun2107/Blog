from flask import Blueprint

bp = Blueprint('auth',__name__)

from myblog.auth import routes