from flask import Blueprint, render_template

from plan.conf.boost import db

bp_home_routes = Blueprint("bp_home_routes", __name__)


@bp_home_routes.route("/")
def home():
    return render_template("home/welcome.html")
