from flask import Blueprint, url_for, render_template, redirect, request, flash
from . import db
from .models import Article, User
from .forms import ArticleForm
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    articles = Article.query.all()
    return render_template('main/index.html', articles=articles)


@main.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        article = Article(title=article_form.title, body=article_form.body, author_id=current_user.id)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('main/create')


@main.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    article_form = ArticleForm()
    if article_form.validate():

        return redirect(url_for('index'))

    return render_template('main/update')


