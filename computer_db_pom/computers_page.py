from computer_db_pom.common.base_page import BasePage


class ComputersPage(BasePage):
    TITLE = 'Computers database'
    URI = '/computers'
    MAIN_CONTENT_ELEMENT_ID = 'main'
    ACTIONS_HEADER_ELEMENT_ID = 'actions'
    COMPUTERS_TABLE_CLASS_NAME = 'computers zebra-striped'

    def __init__(self, web_driver):
        super().__init__(web_driver, self.TITLE, self.URI)

    def get_main_content(self):
        return self.get_element_by_id(self.MAIN_CONTENT_ELEMENT_ID)

    def has_main_content(self):
        return bool(self.get_main_content())

    def get_action_header(self):
        return self.get_element_by_id(self.ACTIONS_HEADER_ELEMENT_ID)

    def has_action_header(self):
        return bool(self.get_action_header())

    def has_page_content(self):
        return self.has_main_content() and self.has_action_header()
