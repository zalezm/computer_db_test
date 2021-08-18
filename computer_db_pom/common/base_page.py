from selenium import webdriver


class BasePage(object):
    def __init__(self, web_driver: webdriver, title: str, uri: str):
        self.title = title
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

    def has_expected_title(self):
        return self.has_title() and self._web_driver.title == self.title
