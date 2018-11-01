#!/bin/env python3

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from csv import writer, QUOTE_MINIMAL


def get_page(url):
    with get(url, stream=True) as src:
        return src.content


def parse_judges(html):
    bs = BeautifulSoup(html, 'lxml')
    html = bs.find('div', {'id': 'ctl00_ctl00_MainEditable_mainContent_RadEditor1'})

    j_type = ' '
    for j in html.findAll(['span', ['table', {'class': 'justicetable'}]]):

        if j.__str__().startswith('<span'):
            j_text = j.text
            if 'justic' in j_text.lower():
                j_type = j_text

        elif j.__str__().startswith('<table'):

            rows = j.findAll('tr')
            header = rows[0].findAll('th')

            J = [['Given Name', 'Sur Name'] + [h.text for h in header[2:]] + ['Position']]
            for r in rows[1:]:
                cols = r.findAll('td')

                if cols[0].a:
                    j_href = cols[0].a['href']
                    first_col = cols[0].a
                else:
                    first_col = cols[0]

                last_name, first_name = first_col.text.__str__().split(',', maxsplit=1)
                J.append([first_name, last_name] + [i.text for i in cols[1:]] + [j_type[:-1]])

    return J


def create_csv(data, csv_file_path='us_supreme_justices'):
    with open(csv_file_path + '.csv', 'w') as csv_file:
        f = writer(csv_file, delimiter=',', quotechar='"', quoting=QUOTE_MINIMAL)
        for i in data:
            f.writerow(i)


def get_domain():
    pass
