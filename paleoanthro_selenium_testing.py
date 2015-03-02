#!/usr/bin/env python 

from selenium import webdriver
from selenium_testing_util import Tester

####################
# Global variables #
####################

tester = Tester()

####################
# Test definitions #
####################

#
## Home page tests
#

# Arbitrarily defining the banner links tests with the home tests
def banner_links_nav_check():
    links = (
                ('//nav[@id="mainmenu"]//a[text()="home"]', \
                    'http://www.paleoanthro.org/home/'),
                ('//nav[@id="mainmenu"]//a[text()="meetings"]', \
                    'http://www.paleoanthro.org/meetings/'),
                ('//nav[@id="mainmenu"]//a[text()="journal"]', \
                    'http://www.paleoanthro.org/journal/'),
                ('//nav[@id="mainmenu"]//a[text()="members"]', \
                    'http://www.paleoanthro.org/members/'),
                ('//nav[@id="mainmenu"]//a[text()="dissertations"]', \
                    'http://www.paleoanthro.org/dissertations/'),
                ('//nav[@id="mainmenu"]//a[text()="students"]', \
                    'http://www.paleoanthro.org/students/')
            )

    print 'banner_links_nav_check: ' + tester.links_nav_check(links)

#######################
# Page test groupings #
#######################

home = (banner_links_nav_check,)

######################
# Run configurations #
######################

browsers = (webdriver.Chrome,)
pages = (
            (home, 'http://www.paleoanthro.org/home/'),
        )

if __name__ == '__main__':
    tester.run_test_suite(browsers, pages)