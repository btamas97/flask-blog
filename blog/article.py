from flask import Blueprint, url_for, render_template, redirect, request, flash
from . import db
from .models import Article, Comment, User
from .forms import CommentForm
from flask_login import login_required, current_user

article = Blueprint('article', __name__)


@article.route('/article/<int:id>', methods=['GET', 'POST'])
def show_full(id):
    full_article = Article.query.filter_by(id=id).first()
    if full_article:
        comments = Comment.query.filter_by(article_id=id).all()
    else:
        flash(message="No article found with such id")
        return redirect(url_for('main.index'))

    return render_template('article/single_article.html', article=full_article, comments=comments)


@article.route('/article/<int:id>/comment', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        body = comment_form.body
        author_id = current_user.id
        article_id = id
        new_comment = CommentForm(body=body, author_id=author_id, article_id=article_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('article.show_full', id=id))

    return render_template('article/comment.html')


