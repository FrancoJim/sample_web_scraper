#!/bin/env/ python3

'''
Using MechanicalSoup
[](https://github.com/MechanicalSoup/MechanicalSoup)
'''

import mechanicalsoup
from bs4 import BeautifulSoup


def google_search_web_scrape():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.reddit.com/search?q=Thanks%20for%20all%20the%20fish")

    html = browser.get_current_page()

    soup = BeautifulSoup(html, 'html.parser')
    # todo: Mechanical Soup seems to be a little buggy.
    print(soup.prettify())
