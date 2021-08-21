from computer_db_pom.components.common.base_component import BaseComponent
from selenium import webdriver


class ComputersTable(BaseComponent):
    COMPUTERS_TABLE_CLASS_NAME = 'computers'
    COMPUTERS_TABLE_BODY_TAG_NAME = 'tbody'
    COMPUTERS_TABLE_ROW_TAG_NAME = 'tr'

    def __init__(self, web_driver: webdriver):
        super().__init__(web_driver)

    def get_computers_table(self):
        return self._call_with_except_block(
            'Unable to retrieve computers table',
            self._web_driver.find_element_by_class_name,
            [self.COMPUTERS_TABLE_CLASS_NAME])

    def has_computers_table(self):
        return bool(self.get_computers_table())

    def get_computers_table_body(self):
        return self._call_with_except_block(
            'Unable to retrieve computers table body',
            self.get_computers_table().find_element_by_tag_name,
            [self.COMPUTERS_TABLE_BODY_TAG_NAME])

    def get_computers_table_rows(self):
        return self._call_with_except_block(
            'Unable to retrieve computers table rows',
            self.get_computers_table_body().find_elements_by_tag_name,
            [self.COMPUTERS_TABLE_ROW_TAG_NAME])
