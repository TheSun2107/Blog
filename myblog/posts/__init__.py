from flask import Blueprint

bp = Blueprint('posts',__name__)

from myblog.posts import routes