# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import sys
import geocoder

from flask import Flask, render_template

from chargin import commands, public, user
from chargin.extensions import (
    bcrypt,
    cache,
    csrf_protect,
    db,
    debug_toolbar,
    login_manager,
    migrate,
    webpack,
)
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__, template_folder=".")

import csv
from collections import defaultdict

with open('./data.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    data_map = defaultdict(list)
    for row in list(readCsv)[1:]:
        data_map["id"].append(row[0])
        data_map["date"].append(row[1])
        data_map["time"].append(row[2])
        data_map["geo_code"].append(row[3])
        data_map["crime_category"].append(row[4])
        data_map["address"].append(row[5])

print(data_map)

def create_app(config_object="chargin.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    configure_logger(app)
    GoogleMaps(app, key="AIzaSyCSkHsXrtRhNDd-5pn0aLk4l7HjsNUtdQY")
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    webpack.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template("{0}.html".format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db, "User": user.models.User}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)

@app.route('/map')
def map_unbounded():
    """Create map with markers out of bounds."""
    locations = []    # long list of coordinates

    for i in range(data_map['id']):
        addr = data_map['id'][i]
        locations = [..., geocoder.google(addr)]
    print(locations)
    map = Map(
        # lat=locations[0].latitude,
        # lng=locations[0].longitude,
        markers=[(loc.latitude, loc.longitude) for loc in locations]
    )
    return render_template('home.html', mymap=map)
