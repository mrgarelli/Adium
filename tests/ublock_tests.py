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
        options.add_argument("--load-extension=" + str(ublock_path))
        options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904 Safari/537.36')

        try:
            browser = webdriver.Chrome(executable_path=self.driver_path, chrome_options=options)
        except Exception as e: raise(e)

        return browser

    def run_tests(self):
        # check nytimes.com
        browser = self.get_new_browser()
        checks_failed = 0
        checks_passed = 0

        # check nytimes.com for ads
        try:
            browser.get('https://www.nytimes.com')
            nytimes_check = browser.find_elements_by_xpath("//a[@href='#after-dfp-ad-top']")
            if nytimes_check:
                checks_failed += 1
        except Exception as e:
            checks_passed += 1
            pass

        # check reddit for ads
        try:
            browser.get('https://www.reddit.com')
            if 'promotedlink' in browser.page_source:
                checks_failed += 1
        except Exception as e:
            checks_passed += 1
            pass

        # check google results page for ads
        try:
            browser.get('https://www.google.com/search?ei=fZOxXv3FJIHg-gTZ6JCwBQ&q=bike+gloves&oq=bike+gloves&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEc6BwgAEIMBEEM6BAgAEENQnzRYr0JgvENoAHADeACAAUqIAbEFkgECMTGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwi9-JzGkZ3pAhUBsJ4KHVk0BFYQ4dUDCAw&uact=5')
            if 'Ad' in browser.page_source:
                checks_failed += 1
        except Exception as e:
            checks_passed += 1
            pass

        browser.quit()
        if checks_failed > 0:
            return False
        else:
            return True
