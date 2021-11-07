from flask.helpers import url_for
from myblog import db
from flask import render_template, flash, redirect
from myblog.posts.forms import PostForm
from flask_login import current_user, login_required
from myblog.models import Post
from myblog.posts import bp

@bp.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))
    return render_template("posts/create_post.html", title='Create Post', form=form)
