Feature: Comptuer Database Portal is reachable and displays default web content

  Scenario Outline: Visiting the Computer Databasae Portal
    Given I open a <browser_type> web browser
    When I load the Computer Database Portal into the web browser
    Then I should see the Computer Database landing page

    Examples:
    | browser_type |
    | Chrome       |
