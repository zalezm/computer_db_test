Feature: Computers Database home page displays all known computers,
  allows users to search for computers, and lets users add a computer.
  Users can also click on computer entries to see its detail page.


  Background:
    Given I open a Chrome web browser


  @search
  Scenario Outline: Searching for computers
    Given I see the Computer Database home page
    When I enter "<search_phrase>" in the search box
    And I click the "search submit" button
    Then I should see the Computers Search Results page

  Examples:
    | search_phrase |
    | fake name     |
    | ACE           |
