#!/bin/env python3

import logging as log
from csv import writer, QUOTE_MINIMAL

from bs4 import BeautifulSoup
from requests import exceptions as r_except
from requests import get

'''
Web Scraping utility to pull list of all U.S. Supreme Justices and import to CSV.

'''


# todo: Add some logging and error handling


def get_page(url='https://www.supremecourt.gov/about/members_text.aspx'):
    '''
    Obtains HTML source code from provided URL.
    :param url: Reachable URL. Default: U.S. Government's Supreme Court's Justices
    :return: HTML source code of provided URL.
    :type: str
    :return err: 1
    :type err: integer
    '''

    try:
        with get(url, stream=True) as src:

            # Check if page came back correctly
            if src.status_code == 200:
                return src.content
            else:
                log.warning('Unable to pull URL.\nStatus code: {}'.format(src.status_code))
    except (r_except.InvalidURL, r_except.MissingSchema) as e:
        log.error('URL is invalid.\nPlease, check URL string and try again.\nerr: {}'.format(e.__str__()))
    except r_except.ConnectionError as e:
        log.error('URL is unreachable.\nPlease, check URL string  and connection, then try again.\nerr: {}'.format(
            e.__str__()))
    except Exception as e:
        log.error('Unexpected issue while pulling url: {}\nerr: {}'.format(url, e.__str__()))
    return 1


def parse_judges(html):
    '''
    Parses source code of U.S. Supreme Justices to do following:
    - Extract all justices, while retaining position in SC
    - Identify if justice has a URL for more information on justice.
    - Split justice's name to given and sur names.

    :param html: HTML Source code
    :return: CSV formatted list of justices.
    :type: Nested lists within list. i.e. [[Header row, ...], [Data row(s), ...], ...]
    '''
    bs = BeautifulSoup(html, 'lxml')
    html = bs.find('div', {'id': 'ctl00_ctl00_MainEditable_mainContent_RadEditor1'})

    Judge_lst, j_type, h_status = [], ' ', 0

    for j in html.findAll(['span', ['table', {'class': 'justicetable'}]]):

        if j.__str__().startswith('<span'):
            j_text = j.text
            if 'justic' in j_text.lower():
                j_type = j_text

        elif j.__str__().startswith('<table'):
            rows = j.findAll('tr')
            header = rows[0].findAll('th')

            if h_status == 0:
                Judge_lst.append(['Given Name', 'Sur Name'] + [h.text for h in header[2:]] + ['Position', 'URL Link'])
                h_status = 1

            for r in rows[1:]:
                cols = r.findAll('td')

                if cols[0].a:
                    j_href = 'https://www.supremecourt.gov/' + cols[0].a['href']
                    first_col = cols[0].a
                else:
                    j_href = ''
                    first_col = cols[0]

                sur_name, given_name = first_col.text.__str__().split(',', maxsplit=1)
                Judge_lst.append([given_name, sur_name] + [i.text for i in cols[1:]] + [j_type[:-1], j_href])
    return Judge_lst


def create_csv(data, csv_file_path='us_supreme_justices'):
    '''
    Imports data to CSV file.
    :param data: List of lines to import into CSV.
    :type data: Nested list(s) within list. i.e. [[Header row, ...], [Data row(s), ...], ...]
    :param csv_file_path: File name and path for output file.
    :type csv_file_path: str
    :return: None
    '''

    with open(csv_file_path + '.csv', 'w') as csv_file:
        f = writer(csv_file, delimiter=',', quotechar='"', quoting=QUOTE_MINIMAL)
        for i in data:
            try:
                f.writerow(i)
            except Exception as e:
                log.error("Unable to write line to {csv_file}. err: {err}".format(**{'csv_file': csv_file_path + '.csv',
                                                                                     'err': e.__str__()}
                                                                                  )
                          )


if __name__ == '__main__':
    html = get_page()
    judge_list = parse_judges(html)
    create_csv(judge_list)
