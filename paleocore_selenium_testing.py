#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium_testing_util import Tester

# TODO: Test results should be printed to a log file, rather than to stdout

####################
# Global variables #
####################

tester = Tester()

####################
# Test definitions #
####################

#
# Home page tests
#

# Arbitrarily defining the banner links tests with the home tests


def banner_links_nav_check():
    links = (
        ('//nav[@id="nav"]//a[text()="Home"]',
         'http://paleocore-qa.tacc.utexas.edu/'),
        ('//nav[@id="nav"]//a[text()="About"]',
         'http://paleocore-qa.tacc.utexas.edu/about/'),
        ('//nav[@id="nav"]//a[text()="Workshops"]',
         'http://paleocore-qa.tacc.utexas.edu/workshops/'),
        ('//nav[@id="nav"]//a[text()="Tools"]',
         'http://paleocore-qa.tacc.utexas.edu/tools/'),
        ('//nav[@id="nav"]//a[text()="Standard"]',
         'http://paleocore-qa.tacc.utexas.edu/standard/'),
        ('//nav[@id="nav"]//a[text()="Projects"]',
         'http://paleocore-qa.tacc.utexas.edu/projects/')
    )

    print 'banner_links_nav_check: ' + tester.links_nav_check(links)


def home_links_nav_check():
    links = (
        ('//h2[text()="About PaleoCore"]/..//a[text()="More..."]',
         'http://paleocore-qa.tacc.utexas.edu/about/'),
        ('//h2[text()="Community"]/..//a[text()="More..."]',
         'http://paleocore-qa.tacc.utexas.edu/workshops/'),
        ('//h2[text()="Tools"]/..//a[text()="More..."]',
         'http://paleocore-qa.tacc.utexas.edu/tools/'),
        ('//h2[text()="Data"]/..//a[text()="More..."]',
         'http://paleocore-qa.tacc.utexas.edu/projects/')
    )

    print 'home_links_nav_check: ' + tester.links_nav_check(links)

# TODO: Possibly add test for clicking on the homepage image


# About page tests


def about_links_nav_check():
    links = (('//h3[text()="Links to Related Projects"]/..' + '//a[text()="eFossils"]',
              'http://www.efossils.org/'),
             ('//h3[text()="Links to Related Projects"]/..' + '//a[text()="eLucy"]',
              'http://www.elucy.org/'),
             ('//h3[text()="Links to Related Projects"]/..' + '//a[text()="eSkeletons"]',
              'http://www.eskeletons.org/'),
             ('//h3[text()="Links to Related Projects"]/..' + '//a[text()="Dublin Core Initiative"]',
              'http://dublincore.org/'),
             ('//h3[text()="Links to Related Projects"]/..' + '//a[text()="TDWG"]',
              'http://www.tdwg.org/'),
             ('//h3[text()="Links to Related Projects"]/..' + '//a[text()="GBIF"]',
              'http://www.gbif.org/')
             )

    print 'about_links_nav_check: ' + tester.links_nav_check(links)


def about_links_content_check():
    links = (
        ('//h2[text()="Our Goals"]/..' + '//a[text()="Read more..."]',
         'http://paleocore-qa.tacc.utexas.edu/about/goals/'),
        # ('//h2[text()="The Name"]/..' + '//a[text()="Access to Biological Collections Data"]',
        #  'https://github.com/tdwg/abcd'),
        # ('//h2[text()="Funding and Support"]/..' + '//a[text()="NSF 1244735"]',
        #  'http://www.nsf.gov/awardsearch/showAward?AWD_ID=1244735'),
    )

    print 'about_links_content_check: ' + tester.links_nav_check(links)


# Tools page tests


def tools_links_nav_check():
    links = (
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Cmap"]',
         'http://cmap.ihmc.us/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Dia"]',
         'https://wiki.gnome.org/action/show/Apps/Dia?action=show&redirect=Dia'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Lucid Chart"]',
         'https://www.lucidchart.com/home/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Protégé"]',
         'http://protege.stanford.edu/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Vue"]',
         'https://vue.tufts.edu/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="ADS"]',
         'http://guides.archaeologydataservice.ac.uk/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Darwin Core"]',
         'http://www.tdwg.org/activities/darwincore/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="here"]',
         'http://rs.tdwg.org/dwc/terms/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Digital Antiquity"]',
         'http://www.digitalantiquity.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Dublin Core"]',
         'http://dublincore.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="TDWG"]',
         'http://www.tdwg.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Arctos"]',
         'http://arctos.database.museum/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="APPA"]',
         'http://www.physanthphylogeny.org/search/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="CODI"]',
         'http://olduvai-paleo.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="eFossils"]',
         'http://efossils.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="eLucy"]',
         'http://www.elucy.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="eSkeletons"]',
         'http://www.eskeletons.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Fieldbook Project"]',
         'http://www.mnh.si.edu/rc/fieldbooks/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Fossilized.org"]',
         'http://fossilized.org/Human_paleontology/index.php'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="GBIF"]',
         'http://www.gbif.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="HADAR Geoinformatics Project"]',
         'https://issrweb.asu.edu/projects/hadar-geoinformatics-project'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="spatial database"]',
         'http://gis1.asurite.ad.asu.edu/hadarv3/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="HERC"]',
         'http://herc.berkeley.edu/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="fossil cast database"]',
         'https://middleawash.berkeley.edu/HERC_specimen_db/main_query.php'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Middle Awash Project Database"]',
         'http://www.fossilized.org/middle_awash/specimen_db/query.php'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Movebank"]',
         'https://www.movebank.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="NEON"]',
         'http://www.neoninc.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="Neotoma"]',
         'http://www.neotomadb.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="PaleoPortal"]',
         'http://www.paleoportal.org/'),
        ('//h3[text()="Data Modeling Tools"]/..//a[text()="VertNet"]',
         'http://www.vertnet.org/index.html'),
    )

    print 'tools_links_nav_check: ' + tester.links_nav_check(links)

#######################
# Page test groupings #
#######################

home = (banner_links_nav_check, home_links_nav_check)
about = (about_links_nav_check, about_links_content_check)
tools = (tools_links_nav_check,)

######################
# Run configurations #
######################

browsers = (webdriver.Chrome,)
pages = (
    (home, 'http://paleocore-qa.tacc.utexas.edu'),
    (about, 'http://paleocore-qa.tacc.utexas.edu/about'),
    (tools, 'http://paleocore-qa.tacc.utexas.edu/tools'),
)


if __name__ == '__main__':
    tester.run_test_suite(browsers, pages)