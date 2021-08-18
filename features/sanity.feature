@sanity
Feature: Computer Database Portal is reachable via web browser and displays default web content
  @SAN01
  Scenario Outline: Loading Computer Database URL in a browser takes me to the home page
    Given I open a <browser_type> web browser
    When I load the Computer Database Portal into the web browser
    Then I should see the Computer Database home page URL

    Examples:
      | browser_type |
      | Chrome       |


  @SAN02
  Scenario Outline: Visiting the Computer Databasae Portal
    Given I open a <browser_type> web browser
    When I load the Computer Database Portal into the web browser
    Then I should see the Computer Database home page

    Examples:
    | browser_type |
    | Chrome       |
