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
from chargin.extensions import login_manager
from chargin.public.forms import LoginForm
from chargin.user.forms import RegisterForm
from chargin.user.models import User
from chargin.utils import flash_errors
import geocoder

blueprint = Blueprint("public", __name__, static_folder="../static")

# you can also pass the key here if you prefer
# GoogleMaps(app)
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__.split(".")[0])

GoogleMaps(app, key="AIzaSyCSkHsXrtRhNDd-5pn0aLk4l7HjsNUtdQY")

import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyCSkHsXrtRhNDd-5pn0aLk4l7HjsNUtdQY"



import csv
from collections import defaultdict

with open('./data2.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    data_map = defaultdict(list)
    for row in list(readCsv)[1:]:
        data_map["id"].append(row[0])
        data_map["date"].append(row[1])
        data_map["time"].append(row[2])
        data_map["geo_code"].append(row[3])
        data_map["crime_category"].append(row[4])
        data_map["address"].append(row[5])
        data_map['latlng'].append((row[len(row) - 2], row[len(row) - 1]))
        # data_map['latitude'].append()
        # data_map['longitude'].append()

# print(data_map['latlng'])
# locations = list()
# for addr in data_map['address'][0:5]:
#     print(addr)
#     locations.append(geocoder.arcgis(addr))
# print(locations[0].json['lat'])



@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    # for addr in :
    #     locations = [..., geocoder.ar(addr)]


    mymap = Map(
        identifier="view-side",  # for DOM element
        varname="mymap",  # for JS object name
        lat=40.110588,
        lng=-88.20727,
        markers=data_map['latlng']
    )

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
    return render_template("public/home.html", form=form, mymap=mymap)


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))


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

@blueprint.route("/")
def mapview():
    """Create map with markers out of bounds."""
    locations = []    # long list of coordinates


    # print(locations)
    mymap = Map(
        identifier="view-side",  # for DOM element
        varname="mymap",  # for JS object name
        lat=40.116421,
        lng=-88.243385,
        markers=[(37.4419, -122.1419)]
    )
    return render_template('public/home.html', mymap=mymap)
