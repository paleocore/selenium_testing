import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

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

#######################
# Page test groupings #
#######################

home = (banner_links_nav_check, home_links_nav_check)

######################
# Run configurations #
######################

browsers = (webdriver.Chrome,)
pages = ((home, 'http://www.paleocore.org'),)

####################
# Global variables #
####################

driver = None
test_url = None

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
			
			driver.get(url)
			check_page_loaded()
		
			for test in tests:
				test()
				driver.get(url)
				check_page_loaded()

	# Closes window and ends program
	driver.quit()
	sys.exit()

##################
# Helper methods #
##################

def check_page_loaded():
	"""
	Helper method that verifies that at least the header of the current page has
	loaded
	"""

	# This should be changed if possible. The difficulty is that it is important
	# that the old page is no longer on the screen.
	sleep(1)

	try:
		waiter = WebDriverWait(driver, 10)
		waiter.until(EC.presence_of_element_located((By.ID, 'header-wrapper')))
	except TimeoutException:
		# TODO: In the future, instead of just printing error, maintain a log
		print 'Paleocore page failed to load'
		driver.quit()
		sys.exit()


def link_check(element_xpath, destination_url):
	"""
	Input: element_xpath- xpath of link element to be tested
		   destination_url- page to which the link should redirect

	Generic method for making sure that links are working properly.
	"""

	try:
		waiter = WebDriverWait(driver, 10)
		link_element = waiter.until(EC.presence_of_element_located((By.XPATH,
																element_xpath)))
	except TimeoutException:
		return 'Element with xpath of \"' + element_xpath + '\" not found'

	link_element.click()
	check_page_loaded()

	if driver.current_url != destination_url:
		return 'Element with xpath of \"' + element_xpath + '\" led to ' + \
			    driver.current_url + ' instead of ' + destination_url


def links_nav_check(links):
	test_results = 'pass'

	for (xpath, destination) in links:
		link_result = link_check(xpath, destination)

		if link_result:
			test_results = 'fail'

			test_results += '\n\t' + link_result

		driver.get(test_url)
		check_page_loaded()

	return test_results


if __name__ == "__main__":
	main()