from computer_db_pom.pages.common.base_page import BasePage


class AddComputerPage(BasePage):
    URI = '/computers/new'

    def __init__(self, web_driver):
        super().__init__(web_driver, self.URI)
