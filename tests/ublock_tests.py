#!/usr/bin/env python3

import os, time
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
        self.browser = self.get_new_browser()
        self.results = []

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

    def run_check(self, url, check):
        # check nytimes.com for ads
        self.browser.get(url)
        time.sleep(3)
        result = 'FAILED' if check() else 'PASSED'
        print('[{}] '.format(result) + check.__name__)
        self.results.append(True if result == 'PASSED' else False)

    def run_tests(self):
        def ny_times_check():
            try:
                self.browser.find_elements_by_xpath("//a[@href='#after-dfp-ad-top']")
            except: return False
            return True
        self.run_check('https://www.nytimes.com', ny_times_check)


        def reddit_check():
            if 'promotedlink' in self.browser.page_source: return True
            return False
        self.run_check('https://www.reddit.com', reddit_check)


        def google_check():
            if 'Ad' in self.browser.page_source: return True
            return False
        self.run_check(
            'https://www.google.com/search?ei=fZOxXv3FJIHg-gTZ6JCwBQ&q=bike+gloves&oq=bike+gloves&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEc6BwgAEIMBEEM6BAgAEENQnzRYr0JgvENoAHADeACAAUqIAbEFkgECMTGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwi9-JzGkZ3pAhUBsJ4KHVk0BFYQ4dUDCAw&uact=5',
            google_check
            )

        self.browser.quit()
        return all(self.results)
