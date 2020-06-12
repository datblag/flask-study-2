from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_moment import Moment
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'eeeeeeeeeeeee'
moment = Moment(app)

class Name(FlaskForm):
    name = StringField('Введите имя:', validators=[DataRequired()])
    submit = SubmitField('Ok')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = Name()
    current_time = datetime.datetime.utcnow()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('user', username=session.get('name')))
    return render_template('index.html', name=session.get('name'), page_header='Hello word', current_time=current_time, form=form)


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', page_header=username)


@app.errorhandler(404)
def error404(e):
    return render_template('404.html',page_header='Page not found'), 404

