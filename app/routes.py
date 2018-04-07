from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'Kai Da Wei'},
            'posttitle': 'Beginner Goals for HTML/CSS/JS',
            'body': 'Becoming a Top Gun HTML/CSS/JS Web Dev means practicing to certain knowledge'
        },
        {
            'author': {'username': 'Kai Da Wei'},
            'postitle': 'The Purpose and Audience for OpenApprentice',
            'body': 'We will help people learn the actual skills and employees know new hires know.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/blog')
def blog():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'Kai Da Wei'},
            'posttitle': 'Beginner Goals for HTML/CSS/JS',
            'body': 'Becoming a Top Gun HTML/CSS/JS Web Dev means practicing to certain knowledge'
        },
        {
            'author': {'username': 'Kai Da Wei'},
            'postitle': 'The Purpose and Audience for OpenApprentice',
            'body': 'We will help people learn the actual skills and employees know new hires know.'
        }
    ]
    return render_template('blog.html', title='blog', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
