from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html', page_header='Hello world')


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', user=username)


@app.errorhandler(404)
def page_404(e):
    return render_template('404.html',  page_header='Page not found'), 404


if __name__ == '__main__':
    app.debug = True
    app.run()
