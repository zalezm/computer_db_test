from behave import given, when, then
from selenium import webdriver
import os
from enum import Enum
from time import sleep
from computer_db_pom.home_page import HomePage

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
    context.web_driver.get(COMPUTER_DATABASE_URL)
    sleep(3)
    print(context.web_driver.title)
    sleep(3)


@then(u'I should see the Computer Database landing page')
def step_impl(context):
    assert context.web_driver.title == HomePage.TITLE, \
        'Expecting home page title {}, got {}'.format(HomePage.TITLE, context.web_driver.title)
