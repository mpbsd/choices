import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname("plan"))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "plan/data/disciplines.db"
    )
