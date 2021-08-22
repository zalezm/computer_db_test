from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse
from abc import ABC


class BasePage(ABC):
    URL = 'https://computer-database.herokuapp.com'
    TITLE = 'Computers database'

    def __init__(self, web_driver: webdriver, uri: str):
        self.title = self.TITLE
        self._web_driver = web_driver
        self.uri = uri

    def load_url(self, url: str):
        try:
            self._web_driver.get(url)
        except Exception as e:
            print('Failed to load url {}: {}'.format(url, e))
            return False

        return True

    def has_title(self):
        return hasattr(self._web_driver, 'title')

    def get_title(self):
        return self._web_driver.title if self.has_title() else None

    def has_expected_title(self):
        return self.has_title() and self.get_title() == self.title

    def has_uri(self):
        return bool(self.get_uri())

    def get_uri(self):
        return urlparse(self._web_driver.current_url).path

    def has_expected_uri(self):
        return self.get_uri() == self.uri

    def has_url(self):
        return bool(self.get_url())

    def get_url(self):
        return urlparse(self._web_driver.current_url).geturl()

    def get_element_by_id(self, element_id: str):
        try:
            return self._web_driver.find_element_by_id(element_id)
        except NoSuchElementException as e:
            print('Element ID {} was not found on page: {}'.format(element_id, e))

        return None
