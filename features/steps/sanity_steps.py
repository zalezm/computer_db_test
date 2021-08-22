from behave import given, when, then
from selenium import webdriver
import os
from enum import Enum
from time import sleep
from computer_db_pom.pages.computers_page import ComputersPage

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
    assert context.current_page.load_url(ComputersPage.URL), 'Failed to load URL {}'.format(ComputersPage.URL)
    # TODO: remove static sleep
    sleep(3)
    print('Current URL: {}'.format(context.web_driver.current_url))


@then(u'I should see the Computer Database home page URL')
def step_impl(context):
    expected_url = ComputersPage.URL + context.current_page.URI
    print(expected_url)
    print(context.current_page.get_url())

    assert expected_url == context.current_page.get_url(), \
        'Expecting URL {}; got {}'.format(expected_url, context.current_page.get_url())
    # TODO: remove static sleep
    sleep(2)
