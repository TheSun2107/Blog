from flask import Blueprint

bp = Blueprint('main',__name__)

from myblog.main import routes