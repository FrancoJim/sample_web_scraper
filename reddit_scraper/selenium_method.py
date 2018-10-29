#!/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from bs4 import BeautifulSoup as bs


def selenium_reddit_scrape():
    # driver = webdriver.Firefox()
    # options = webdriver.FirefoxOptions()
    # options.add_argument("--test-type")
    # options.binary_location = "/usr/bin/chromium"

    # driver.get("http://www.reddit.com")

    try:
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header-search-bar"]')))
        #
        # elem = driver.find_element_by_xpath('//*[@id="header-search-bar"]')
        #
        # elem.clear()
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        #
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="t3_8j4ep6"]')))
        # html = driver.page_source

        with open('temp.txt', 'r') as f:
            html = f.read()

        soup = bs(html, 'html.parser')

        results = soup.find(id='t3_8j4ep6')

        for s in results.find_all('div'):
            print(s)


    except TimeoutException as e:
        print('uh-oh', e.__str__())

    except Exception as e:
        print('timed out', e.__str__())
    finally:

        driver.quit()
