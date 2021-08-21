from behave import given, when, then
from computer_db_pom.pages.computers_page import ComputersPage
from time import sleep
from urllib.parse import urljoin, urlencode


@given(u'I see the Computer Database home page')
def step_impl(context):
    context.execute_steps(u"""
        when I load the Computer Database Portal into the web browser
        then I should see the Computer Database home page
    """)


@given(u'the search box is empty')
def step_impl(context):
    context.search_phrase = ''
    assert context.current_page.get_action_header().input_search(context.search_phrase), \
        'Failed to enter empty search phrase'


@when(u'I enter "{search_phrase}" in the search box')
def step_impl(context, search_phrase):
    context.search_phrase = search_phrase
    assert context.current_page.get_action_header().input_search(search_phrase), 'Failed to enter search phrase'


@when(u'I click the "{button_name}" button')
def step_impl(context, button_name):
    if button_name == 'search submit':
        assert context.current_page.get_action_header().click_search_submit_button(), \
            'Failed to click search submit button'
    else:
        raise AssertionError('Unknown button {}'.format(button_name))


@then(u'I should see the Computers Search Results page')
def step_impl(context):
    search_phrase = getattr(context, 'search_phrase', '')
    url_query = urlencode({'f': search_phrase})
    expected_url = urljoin(ComputersPage.URL, ComputersPage.URI) + '?{}'.format(url_query)

    assert expected_url == context.current_page.get_url(), \
        'Expecting URL {}; got {}'.format(expected_url, context.current_page.get_url())
    # TODO: remove static sleep
    sleep(2)


@then(u'I should see at least {result_count:d} result')
def step_impl(context, result_count):
    print('Looking for at least {} result count'.format(result_count))
    assert context.current_page.get_computers_table(), 'No computers table found'
    computers_table_elements = context.current_page.get_computers_table().get_computers_table_rows()
    print('Computers table: {}'.format(computers_table_elements))
