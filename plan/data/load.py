#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from pathlib import Path


class Disciplines:
    def __init__(self, year, half):
        self.year = year
        self.half = half
        self.data = Path(
            "plan/data/%4d%02d.db" % (self.year, self.half)
        )

    def list(self):
        dscplns = None
        if self.data.is_file():
            connection = sqlite3.connect(self.data)
            cursor = connection.cursor()
            try:
                response = cursor.execute("SELECT * FROM discipline")
                dscplns = response.fetchall()
            except sqlite3.OperationalError as errormsg:
                print(errormsg)
        return dscplns

    def __repr__(self):
        return f"Encargos didáticos do IME/UFG em {self.year}/{self.half}"


def main():
    dscplns = Disciplines(2024, 2)
    print(dscplns.list())


if __name__ == "__main__":
    main()
