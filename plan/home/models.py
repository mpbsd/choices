import sqlalchemy as sa
import sqlalchemy.orm as so

from plan.conf.boost import db


class Discipline(db.Model):
    campus: so.Mapped[str] = so.mapped_column(sa.String(9), primary_key=True)
    discipline: so.Mapped[str] = so.mapped_column(
        sa.String(38), primary_key=True
    )
    department: so.Mapped[str] = so.mapped_column(
        sa.String(24), primary_key=True
    )
    schedule: so.Mapped[str] = so.mapped_column(sa.String(6), primary_key=True)
