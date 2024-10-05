import sqlalchemy as sa
from flask import Blueprint, render_template

from plan.conf.boost import db
from plan.home.models import Discipline

bp_home_routes = Blueprint("bp_home_routes", __name__)


@bp_home_routes.route("/")
def home():
    disciplines = db.session.scalars(
        sa.select(Discipline).order_by(Discipline.schedule)
    ).all()
    return render_template("home/welcome.html", disciplines=disciplines)
