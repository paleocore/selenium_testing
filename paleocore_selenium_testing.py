import sys, time
# from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

# TODO: Test results should be printed to a log file, rather than to stdout

####################
# Global variables #
####################

driver = None
test_url = None

############################
# Useful class definitions #
############################

# TODO: Move this to a place where it actually belongs
def wait_for(condition_function):
    start_time = time.time()
    
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)

    raise Exception('Timeout waiting for {}'.format(condition_function.__name__))

# Credit for this extremely useful class:
# http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html
class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for(self.page_has_loaded)

####################
# Test definitions #
####################

#
## Home page tests
#

# Arbitrarily defining the banner links tests with the home tests
def banner_links_nav_check():
	links = (
				('//nav[@id="nav"]//a[text()="Home"]',
					'http://www.paleocore.org/'),
				('//nav[@id="nav"]//a[text()="About"]',
					'http://www.paleocore.org/about/'),
				('//nav[@id="nav"]//a[text()="Workshops"]',
					'http://www.paleocore.org/workshops/'),
				('//nav[@id="nav"]//a[text()="Data"]',
					'http://www.paleocore.org/data/'),
				('//nav[@id="nav"]//a[text()="Tools"]',
					'http://www.paleocore.org/tools/')
			)

	print 'banner_links_nav_check: ' + links_nav_check(links)


def home_links_nav_check():
	links = (
				('//h2[text()="About PaleoCore"]/..//a[text()="More..."]',
					'http://www.paleocore.org/about/'),
				('//h2[text()="Community"]/..//a[text()="More..."]',
					'http://www.paleocore.org/workshops/'),
				('//h2[text()="Tools"]/..//a[text()="More..."]',
					'http://www.paleocore.org/tools/'),
				('//h2[text()="Data"]/..//a[text()="More..."]',
					'http://www.paleocore.org/data/')
			)

	print 'home_links_nav_check: ' + links_nav_check(links)

# TODO: Possibly add test for clicking on the homepage image

#
## About page tests
#

def about_links_nav_check():
	links = (
				('//h3[text()="Links to Related Projects"]/..' + \
										'//a[text()="Dublin Core Initiative"]',
					'http://dublincore.org/'),
				('//h3[text()="Links to Related Projects"]/..' + \
										'//a[text()="TDWG"]',
					'http://www.tdwg.org/'),
				('//h3[text()="Links to Related Projects"]/..' + \
										'//a[text()="GBIF"]',
					'http://www.gbif.org/')
			)

	print 'about_links_nav_check: ' + links_nav_check(links)

#######################
# Page test groupings #
#######################

home = (banner_links_nav_check, home_links_nav_check)
about = (about_links_nav_check,)

######################
# Run configurations #
######################

browsers = (webdriver.Chrome,)
pages = (
			(home, 'http://www.paleocore.org'),
			(about, 'http://www.paleocore.org/about'),
		)

###############
# Main method #
###############

def main():
	"""
	Main method for running the front-end test suite for paleocore.org
	"""
	
	for browser in browsers:
		global driver
		driver = browser()
		driver.implicitly_wait(1)

		for (tests, url) in pages:
			global test_url
			test_url = url
		
			for test in tests:
				driver.get(url)
				test()

	# Closes window and ends program
	driver.quit()
	sys.exit()

##################
# Helper methods #
##################

def link_check(element_xpath, destination_url):
	"""
	Input:  element_xpath- xpath of link element to be tested
		   	destination_url- page to which the link should redirect
	Output: None if element at element_xpath redirected to destination_url,
			otherwise a string of some error text

	Generic method for making sure that links are working properly.
	"""

	with wait_for_page_load(driver):
		driver.find_element_by_xpath(element_xpath).click()

	if driver.current_url != destination_url:
		return 'Element with xpath of \"' + element_xpath + '\" led to ' + \
		    	driver.current_url + ' instead of ' + destination_url


def links_nav_check(links):
	"""
	Input:  links- tuples of string pairs for each link on a page to be checked
			contained in a tuple
	Output: A string of the test results, with error details if there was a
			failure

	Method for checking a group of links defined in a test.
	"""

	test_results = 'pass'

	for (xpath, destination) in links:
		link_result = link_check(xpath, destination)

		if link_result:
			test_results = 'fail'

			test_results += '\n\t' + link_result

		driver.get(test_url)

	return test_results


if __name__ == "__main__":
	main()