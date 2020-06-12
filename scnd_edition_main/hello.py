from flask import Flask, render_template, redirect, url_for, session, flash
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('Введите ваше имя:', validators=[DataRequired()])
    submit = SubmitField('Ok')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Attention! You change name!")
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('user', username=session.get('name')))
    form.name.data = ''
    return render_template('index.html', name=session.get('name'), page_header='Hello world', current_time=datetime.datetime.utcnow(), form=form)


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', user=username)

@app.route('/logout/')
def logout():
    session['name'] = None
    return redirect('/')


@app.errorhandler(404)
def page_404(e):
    return render_template('404.html',  page_header='Page not found'), 404


if __name__ == '__main__':
    app.debug = True
    app.run()
