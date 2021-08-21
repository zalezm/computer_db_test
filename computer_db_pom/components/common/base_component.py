from selenium import webdriver
from abc import ABC


class BaseComponent(ABC):
    def __init__(self, web_driver: webdriver):
        self._web_driver = web_driver

    def get_element_by_id(self, element_id: str):
        return self._call_with_except_block(
            'Element ID {} was not found on page: '.format(element_id),
            self._web_driver.find_element_by_id, [element_id])

    @staticmethod
    def _call_with_except_block(fail_message, func, args=[]):
        try:
            return func(*args)
        except Exception as e:
            print(fail_message + ': {}'.format(e))

        return None
