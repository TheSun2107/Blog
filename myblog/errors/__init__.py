from flask import Blueprint

bp = Blueprint('errors',__name__)

from myblog.errors import handlers