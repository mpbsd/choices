#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from pathlib import Path


class Disciplines:
    def __init__(self, year, semester):
        self.year = year
        self.semester = semester
        self.database = Path(
            "plan/data/%4d%02d.db" % (self.year, self.semester)
        )

    def list(self):
        dscplns = None
        if self.database.is_file():
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            try:
                response = cursor.execute("SELECT * FROM discipline")
                dscplns = response.fetchall()
            except sqlite3.OperationalError as errormsg:
                print(errormsg)
        return dscplns

    def __repr__(self):
        return f"Encargos didáticos do IME/UFG em {self.year}/{self.semester}"


def main():
    dscplns = Disciplines(2024, 2)
    print(dscplns.list())


if __name__ == "__main__":
    main()
