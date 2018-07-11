from flask import render_template, flash, redirect, url_for, request
from application import application
from application.forms import LoginForm, ContactForm
from flask_bootstrap import Bootstrap
from flask_login import current_user, login_user, logout_user, login_required
from application.models import User
from werkzeug.urls import url_parse
from application.email import send_contact_info_email
from datetime import datetime

bootstrap = Bootstrap(application)

@application.route('/')
@application.route('/home')
@application.route('/index')
def index():
    return render_template("home.html", title='Home')

@application.route('/services')
def services():
    return render_template("services.html", title='Services', header='Our Services')

@application.route('/login', methods=['POST', 'GET'])
# The HTTP protocol states that GET requests are those that return information to the client (the web browser in this case)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): #only works (true) for POST request
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Incorrect password or username")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('portfolio_entry')
        flash("Logged in successfully")
        return redirect(next_page)
    return render_template("login.html",  title='Login', form=form, header='Log In')

@application.route('/logout')
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('index'))


@application.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_contact_info_email(datetime.utcnow(), form.name.data, form.phoneNumber.data, form.description.data)
        flash("Thank you, contact information received")
        return redirect(url_for('contact'))
    return render_template("contact.html",  title='Contact', form=form, header='Contact Us')

@application.route('/portfolio')
def portfolio():
    return render_template("portfolio.html",  title='Portfolio', header='Our Portfolio')

@application.route('/new-portfolio-entry')
@login_required
def portfolio_entry():
    return render_template("new-portfolio-entry.html",  title='New Portfolio Entry', header='New Entry')