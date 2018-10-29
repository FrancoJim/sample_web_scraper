#!/bin/env python3

'''
Web Scraping using Grab Library.

[Grab Documentation](https://grablib.org/en/latest/)

NOTE: Library appears to have an issue with version of "six" module.
(2018-10-29)


'''

from grab import Grab

g = Grab()
resp = g.go('http://www.google.com/')
