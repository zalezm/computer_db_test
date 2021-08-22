from behave import given, when, then


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


@then(u'I should see at least {result_count:d} result')
def step_impl(context, result_count):
    print('Looking for at least {} result count'.format(result_count))
    assert context.current_page.get_computers_table(), 'No computers table found'
    computers_table_elements = context.current_page.get_computers_table().get_computers_table_rows()
    print('Computers table: {}'.format(computers_table_elements))
