def create_app():
    from flask import Flask

    plan = Flask(__name__)

    from plan.conf.setup import Config

    plan.config.from_object(Config)

    from plan.conf.boost import db

    db.init_app(plan)

    from plan.conf.boost import migrate

    migrate.init_app(plan, db)

    from plan.home.routes import bp_home_routes

    plan.register_blueprint(bp_home_routes, url_prefix="/")

    return plan
