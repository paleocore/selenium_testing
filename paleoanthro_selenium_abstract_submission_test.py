#!/usr/bin/env python

import os, sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# Author object to make filling in Author information easier
class Author:
    def __init__(self, first_name='Dummy', last_name='Dumbell', \
                 full_name='Dummy Dumbell', department='Department of Dumb', \
                 institution='University of Dumb', country='Zimbabwe', \
                 email='dumb@dumb.com'):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.department = department
        self.institution = institution
        self.country = country
        self.email = email


def main():
    """
    Main method for running the test_results
    """

    # Choose type of driver
    # TODO: Figure out a way to run the tests on multiple browsers in one run.
    driver = webdriver.Chrome()

    driver.get('http://127.0.0.1:8000/meetings/abstract/add/')

    page_loaded(driver)

    # Calling the tests
    simple_valid(driver)
    matching_email(driver)
    full_name(driver)
    no_author(driver)
    over_300_words(driver)
    add_author(driver)
    valid_author_email_address(driver)
    all_authors_filled(driver)

    driver.quit()
    sys.exit()


def required(driver, presentation_type='Poster', title='Dummy title', \
             text='Dummy abstract test', contact_email='dummy@dummy.com', \
             confirm_email='dummy@dummy.com', authors={0: Author()}):
    """
    Method for filling all of the required fields, with either default or 
    specifically defined values
    """

    if presentation_type is not None:
        presentation_selector = driver.find_element_by_id('id_presentation_type')
        Select(presentation_selector).select_by_value(presentation_type)

    if title is not None:
        driver.find_element_by_id('id_title').send_keys(title)

    if text is not None:
        driver.find_element_by_id('id_abstract_text').send_keys(text)

    if contact_email is not None:
        driver.find_element_by_id('id_contact_email').send_keys(contact_email)
    if confirm_email is not None:
        driver.find_element_by_id('id_confirm_email').send_keys(confirm_email)

    if authors is not None:
        for key in authors.keys():
            fill_author(driver, key, authors[key])


def fill_author(driver, author_number, author):
    """
    Helper method for filling in an author's fields
    """

    if author.first_name is not None:
        driver.find_element_by_id('id_author_set-' + str(author_number) + \
                                  '-last_name').send_keys(author.first_name)
    if author.last_name is not None:
        driver.find_element_by_id('id_author_set-' + str(author_number) + \
                                  '-first_name').send_keys(author.last_name)
    if author.full_name is not None:
        driver.find_element_by_id('id_author_set-' + str(author_number) + \
                                  '-name').send_keys(author.full_name)

    if author.department is not None:
        driver.find_element_by_id('id_author_set-' + str(author_number) + \
                                  '-department').send_keys(author.department)
    if author.institution is not None:
        driver.find_element_by_id('id_author_set-' + str(author_number) + \
                                  '-institution').send_keys(author.institution)

    if author.country is not None:
        country_select = driver.find_element_by_id('id_author_set-' + \
                                                   str(author_number) + \
                                                   '-country')
        Select(country_select).select_by_value(author.country)

    if author.email is not None:
        driver.find_element_by_id('id_author_set-' + str(author_number) + \
                                  '-email_address').send_keys(author.email)

############################
## Begin Test Definitions ##
############################

def simple_valid(driver):
    required(driver)

    test_results('Thanks', 'simple_valid', driver)


def no_author(driver):
    required(driver, authors=None)

    test_results('Create Abstract', 'no_author', driver)


def over_300_words(driver):
    to_send = ''

    for i in range(0, 400):
        to_send += 'word '

    required(driver, text=to_send)

    test_results('Create Abstract', 'over_300_words', driver)


def matching_email(driver):
    required(driver, contact_email='dumb@dumb.com', \
             confirm_email='dummer@dumb.com')

    test_results('Create Abstract', 'matching_email', driver)


def full_name(driver):
    required(driver, authors={0: Author(first_name=None, last_name=None)})

    test_results('Thanks', 'full_name', driver)


def add_author(driver):
    required(driver)

    driver.find_element_by_xpath('//input[@name="add_authors"]').click()

    page_loaded(driver)

    # This is necessary to check that the additional fields appeared.
    try:
        driver.find_element_by_id('id_author_set-3-name')
        print 'add_author: pass'
    except NoSuchElementException:
        print 'add_author: fail'
    finally:
        driver.get('http://127.0.0.1:8000/meetings/abstract/add/')

        page_loaded(driver)


def valid_author_email_address(driver):
    required(driver, authors={0: Author(email='dumb')})

    test_results('Create Abstract', 'valid_author_email_address', driver)


def all_authors_filled(driver):
    required(driver, authors={0: Author(), 1: Author(), 2: Author()})

    test_results('Thanks', 'all_authors_filled', driver)

#########################
## End Test Definition ##
#########################

def test_results(expected_title, test_name, driver):
    """
    This method verifies that the user is redirected to the expected page
    (as defined by the expected title).
    'Thanks' = valid submission
    'Create Abstract = invalid submission'
    """

    driver.find_element_by_xpath('//input[@value="Submit Abstract"]').click()

    sleep(1)

    try:
        assert expected_title == driver.title
        print test_name + ': pass'
    except AssertionError:
        print test_name + ': fail'
    finally:
        driver.get('http://127.0.0.1:8000/meetings/abstract/add/')

        page_loaded(driver)


def page_loaded(driver):
    """
    Helper method to make sure that the abstract creation page has loaded
    successfully before performing any actions on the elements in the page.
    """

    try:
        waiter = WebDriverWait(driver, 60)
        waiter.until(EC.presence_of_element_located((By.ID, \
                                                    'id_presentation_type')))
    except TimeoutException:
        print 'Abstract adding page failed to load'
        driver.quit()
        sys.exit()


if __name__ == "__main__":
    main()