#!/usr/bin/env python 

import sys
from selenium import webdriver
from selenium_testing_util import WaitForPageLoad, GeneralTest

# TODO: Test results should be printed to a log file, rather than to stdout

####################
# Global variables #
####################

driver = None
test_url = None
tester = None

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

	print 'banner_links_nav_check: ' + tester.links_nav_check(links)


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

	print 'home_links_nav_check: ' + tester.links_nav_check(links)

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

	print 'about_links_nav_check: ' + tester.links_nav_check(links)

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
				global tester
				tester = GeneralTest(driver, test_url)

				driver.get(url)	
				test()

	# Closes window and ends program
	driver.quit()
	sys.exit()


if __name__ == "__main__":
	main()