from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, web_driver: webdriver, title: str, uri: str):
        self.title = title
        self._web_driver = web_driver
        self.uri = uri
        self._current_url = None

    def load_url(self, url: str):
        try:
            self._web_driver.get(url)
            self._current_url = urlparse(self._web_driver.current_url)
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
        return self._current_url and self._current_url.path

    def get_uri(self):
        return self._current_url.path if self.has_uri() else None

    def has_expected_uri(self):
        return self.has_uri() and self.get_uri() == self.uri

    def get_element_by_id(self, element_id: str):
        try:
            return self._web_driver.find_element_by_id(element_id)
        except NoSuchElementException as e:
            print('Element ID {} was not found on page: {}'.format(element_id, e))

        return None
