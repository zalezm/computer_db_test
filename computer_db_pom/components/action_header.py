from computer_db_pom.components.common.base_component import BaseComponent


class ActionHeader(BaseComponent):
    ACTIONS_HEADER_ELEMENT_ID = 'actions'
    ACTIONS_SEARCH_BOX_ELEMENT_ID = 'searchbox'
    ACTIONS_SEARCH_SUBMIT_BUTTON_ELEMENT_ID = 'searchsubmit'
    ACTIONS_ADD_COMPUTER_BUTTON_ELEMENT_ID = 'add'

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def get_action_header(self):
        return self.get_element_by_id(self.ACTIONS_HEADER_ELEMENT_ID)

    def has_action_header(self):
        return bool(self.get_action_header())

    def get_search_box(self):
        return self.get_element_by_id(self.ACTIONS_SEARCH_BOX_ELEMENT_ID)

    def has_search_box(self):
        return bool(self.get_search_box())

    def get_search_submit_button(self):
        return self.get_element_by_id(self.ACTIONS_SEARCH_SUBMIT_BUTTON_ELEMENT_ID)

    def has_search_submit_button(self):
        return bool(self.get_search_submit_button())

    def get_add_computer_button(self):
        return self.get_element_by_id(self.ACTIONS_ADD_COMPUTER_BUTTON_ELEMENT_ID)

    def has_add_computer_button(self):
        return bool(self.get_add_computer_button())

    def input_search(self, search_phrase: str):
        search_box = self.get_search_box()

        if search_box:
            print('Entering search phrase {}'.format(search_phrase))
            search_box.send_keys(search_phrase)
            return True
        else:
            print(
                'Missing search elements; search box: {} | search submit: {}'.format(search_box, search_submit_button))

        return False

    def click_search_submit_button(self):
        search_submit_button = self.get_search_submit_button()
        if search_submit_button:
            search_submit_button.click()
            return True
        else:
            print('No search submit button found')

        return False
