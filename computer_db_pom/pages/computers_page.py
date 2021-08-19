from computer_db_pom.pages.common.base_page import BasePage
from computer_db_pom.components.action_header import ActionHeader


class ComputersPage(BasePage):
    TITLE = 'Computers database'
    URI = '/computers'
    MAIN_CONTENT_ELEMENT_ID = 'main'
    COMPUTERS_TABLE_CLASS_NAME = 'computers zebra-striped'

    def __init__(self, web_driver):
        super().__init__(web_driver, self.TITLE, self.URI)
        self._action_header = ActionHeader(web_driver)

    def get_main_content(self):
        return self.get_element_by_id(self.MAIN_CONTENT_ELEMENT_ID)

    def has_main_content(self):
        return bool(self.get_main_content())

    def has_page_content(self):
        return self.has_main_content() and self.get_action_header().has_action_header()

    def get_action_header(self):
        return self._action_header
