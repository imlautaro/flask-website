from flask import Blueprint, render_template

web = Blueprint('web', __name__, static_folder='static', template_folder='templates')

@web.route('/')
def index():
    return render_template('views/index.html')

@web.route('/about')
def about():
    return render_template('views/about.html')

@web.route('/contact')
def contact():
    return render_template('views/contact.html')

@web.route('/blog')
def blog():
    return render_template('views/blog.html')

@web.route('/blog/<slug>')
def article(slug):
    return render_template('views/article.html')
