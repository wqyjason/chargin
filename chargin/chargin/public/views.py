# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    Flask,
)
from flask_login import login_required, login_user, logout_user
from flask_googlemaps import GoogleMaps, Map

from chargin.extensions import login_manager
from chargin.public.forms import LoginForm
from chargin.user.forms import RegisterForm
from chargin.user.models import User
from chargin.utils import flash_errors



blueprint = Blueprint("public", __name__, static_folder="../static")
# GoogleMaps(current_app, key="AIzaSyCk4JwW6dunM69b6Qi-9L0UtEK0jnwUXJk")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))


@blueprint.route("/maps/")
def maps():
    """Map page"""
    # mymap = Map(
    #     identifier="view-side",
    #     lat=37.4419,
    #     lng=-122.1419,
    #     markers=[(37.4419, -122.1419)]
    # )
    # sndmap = Map(
    #     identifier="sndmap",
    #     lat=37.4419,
    #     lng=-122.1419,
    #     markers=[
    #       {
    #          'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    #          'lat': 37.4419,
    #          'lng': -122.1419,
    #          'infobox': "<b>Hello World</b>"
    #       },
    #       {
    #          'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    #          'lat': 37.4300,
    #          'lng': -122.1400,
    #          'infobox': "<b>Hello World from other place</b>"
    #       }
    #     ]
    # )
    # return render_template('/home/jason/Documents/projects/chargin/chargin/chargin/templates/public/maps.html', mymap=sndmap)
    return render_template('public/maps.html')



@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)
