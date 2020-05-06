#!/usr/bin/env python3

import os
from selenium import webdriver

"""
Creates simple browser instance, 
navigates to New York Times home page 
checks for the presence of a banner ad
closes browser instance
    return True if no ads on page
    return False if ads on page
"""

class IntegrationTests:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def get_new_browser(self):

        ublock_path = os.path.dirname(os.path.abspath(__file__))[:-6] + '/build'
        options = webdriver.ChromeOptions()
        # All the arguments added for chromium to work on selenium
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-default-apps")
        options.add_argument("start-maximized")
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("-load-extension=" + str(ublock_path))
        options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904 Safari/537.36')

        try:
            browser = webdriver.Chrome(executable_path=self.driver_path, chrome_options=options)
        except Exception as e: raise(e)

        return browser

    def run_tests(self):
        browser = self.get_new_browser()
        browser.get('https://www.nytimes.com')
        try:
            browser.find_elements_by_xpath("//a[@href='#after-dfp-ad-top']")
            browser.quit()
            return False
        except:
            browser.quit()
            return True