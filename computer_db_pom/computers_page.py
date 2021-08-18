from computer_db_pom.common.base_page import BasePage


class ComputersPage(BasePage):
    TITLE = 'Computers database'
    URI = '/computers'

    def __init__(self, web_driver):
        super().__init__(web_driver, self.TITLE, self.URI)
