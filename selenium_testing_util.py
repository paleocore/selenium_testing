import time, sys
from selenium.common.exceptions import NoSuchElementException

############################
# Useful class definitions #
############################

class WaitForPageLoad(object):
    """
    Credit for this extremely useful class:
    http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html
    """

    def __init__(self, browser):
        self.browser = browser


    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')


    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id


    def __exit__(self, *_):
        wait_for(self.page_has_loaded)


class Tester(object):
    """
    This class is to make the general definitions a little easier
    """

    def link_check(self, element_xpath, destination_url):
        """
        Input:  element_xpath- xpath of link element to be tested
                destination_url- page to which the link should redirect
        Output: None if element at element_xpath redirected to destination_url,
                otherwise a string of some error text

        Generic method for making sure that links are working properly.
        """

        with WaitForPageLoad(self.driver):
            try:
                self.driver.find_element_by_xpath(element_xpath).click()
            except NoSuchElementException:
                # This redirect doesn't really matter, it's just to facilitate
                # exiting the with statement
                self.driver.get(destination_url)
                return 'Element with xpath of ' + element_xpath + ' not found.'

        if self.driver.current_url != destination_url:
            return 'Element with xpath of \"' + element_xpath + '\" led to ' + \
                    self.driver.current_url + ' instead of ' + destination_url


    def links_nav_check(self, links):
        """
        Input:  links- tuples of string pairs for each link on a page to be 
                checked contained in a tuple
        Output: A string of the test results, with error details if there was a
                failure

        Method for checking a group of links defined in a test.
        """

        test_results = 'pass'

        for (xpath, destination) in links:
            link_result = self.link_check(xpath, destination)

            if link_result:
                test_results = 'fail'

                test_results += '\n\t' + link_result

            self.driver.get(self.test_url)

        return test_results


    def run_test_suite(self, browsers, pages):
        for browser in browsers:
            self.driver = browser()
            self.driver.implicitly_wait(1)

            for (tests, url) in pages:
                self.test_url = url

                for test in tests:
                    self.driver.get(url)    
                    test()

        # Closes window and ends program
        self.driver.quit()
        sys.exit()

##################
# Helper methods #
##################

def wait_for(condition_function):
    """
    Necessary for WaitForPageLoad
    """

    start_time = time.time()
    
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)

    raise Exception('Timeout waiting for {}'.format(condition_function.__name__))