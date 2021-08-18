from behave import given, when, then
from selenium import webdriver
import os
from enum import Enum
from time import sleep
from computer_db_pom.computers_page import ComputersPage

COMPUTER_DATABASE_URL = 'https://computer-database.herokuapp.com/'
WEB_DRIVER_DIR = 'web_drivers'


class WebDrivers(Enum):
    CHROME = 'chromedriver.exe'


def get_web_driver_path(web_driver: WebDrivers):
    current_dir = os.getcwd()
    return os.path.join(current_dir, WEB_DRIVER_DIR, web_driver.value)


@given(u'I open a Chrome web browser')
def step_impl(context):
    web_driver_path = get_web_driver_path(WebDrivers.CHROME)
    web_driver_exists = os.path.exists(web_driver_path)
    print('Web driver path: {} exists? {}'.format(web_driver_path, web_driver_exists))
    assert web_driver_exists, 'Web driver path {} does not exist'.format(web_driver_path)
    context.web_driver = webdriver.Chrome(web_driver_path)
    print('Successfully created Chrome webdriver')


@when(u'I load the Computer Database Portal into the web browser')
def step_impl(context):
    context.current_page = ComputersPage(context.web_driver)
    assert context.current_page.load_url(COMPUTER_DATABASE_URL), 'Failed to load URL {}'.format(COMPUTER_DATABASE_URL)
    # TODO: remove static sleep
    sleep(3)
    print('Current URL: {}'.format(context.web_driver.current_url))


@then(u'I should see the Computer Database home page')
def step_impl(context):
    assert context.current_page.has_expected_uri(), \
        'Expecting URI {}, got {}'.format(context.current_page.uri, context.current_page.get_uri())
    assert context.current_page.has_expected_title(), \
        'Expecting home page title {}, got {}'.format(context.current_page.title, context.current_page.get_title())
    assert context.current_page.has_page_content(), 'Page content was not found!'
    # TODO: remove static sleep
    sleep(3)
