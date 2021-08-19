from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from abc import ABC


class BaseComponent(ABC):
    def __init__(self, web_driver: webdriver):
        self._web_driver = web_driver

    def get_element_by_id(self, element_id: str):
        try:
            return self._web_driver.find_element_by_id(element_id)
        except NoSuchElementException as e:
            print('Element ID {} was not found on page: {}'.format(element_id, e))

        return None
