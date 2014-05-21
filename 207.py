#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

if __name__ == '__main__':
    cr = csv.reader(open("207demographie_donnees.csv", "rb"))
    for row in cr:
        print row
