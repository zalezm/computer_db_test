from behave import given, when, then, step
from enum import Enum
from computer_db_pom.pages.search_page import SearchPage
from computer_db_pom.pages.add_computer_page import AddComputerPage
from computer_db_pom.pages.computers_page import ComputersPage
from time import sleep
from urllib.parse import urljoin, urlencode


class Button(Enum):
    SEARCH_SUBMIT = 'search submit'
    ADD_COMPUTER = 'add a new computer'


class Page(Enum):
    COMPUTER_DB = 'Computer Database home'
    SEARCH_RESULTS = 'Computers Search Results'
    ADD_COMPUTER = 'Add Computer'


@when(u'I click the "{button_name}" button')
def step_impl(context, button_name):
    if button_name == Button.SEARCH_SUBMIT.value:
        assert context.current_page.get_action_header().click_search_submit_button(), \
            'Failed to click search submit button'

        search_phrase = getattr(context, 'search_phrase', '')
        encoded_search_phrase = urlencode({'f': search_phrase})[2:]
        context.current_page = SearchPage(context.web_driver, search_phrase, encoded_search_phrase)
    elif button_name == Button.ADD_COMPUTER.value:
        assert context.current_page.get_action_header().click_add_computer_button(), \
            'Failed to click add a computer button'
        context.current_page = AddComputerPage(context.web_driver)
    else:
        raise AssertionError('Unknown button {}'.format(button_name))
    # TODO: remove static sleep
    sleep(1)


@then(u'I should see the {page_type} page')
def step_impl(context, page_type):
    if page_type == Page.COMPUTER_DB.value:
        expected_url = urljoin(ComputersPage.URL, ComputersPage.URI)
        assert context.current_page.has_page_content(), 'Page content was not found!'
    elif page_type == Page.SEARCH_RESULTS.value:
        search_phrase = getattr(context, 'search_phrase', '')
        url_query = urlencode({'f': search_phrase})
        expected_url = urljoin(SearchPage.URL, SearchPage.URI) + '?{}'.format(url_query)
    elif page_type == Page.ADD_COMPUTER.value:
        expected_url = urljoin(AddComputerPage.URL, AddComputerPage.URI)
    else:
        raise AssertionError('Unsupported page type: {}'.format(page_type))

    assert context.current_page.has_expected_title(), \
        'Expecting page title {}, got {}'.format(context.current_page.title, context.current_page.get_title())
    assert expected_url == context.current_page.get_url(), \
        'Expecting URL {}; got {}'.format(expected_url, context.current_page.get_url())
    # TODO: remove static sleep
    sleep(2)
