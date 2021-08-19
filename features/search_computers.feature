@search
Feature: Computers Database home page displays an action header, which allows users
  to search for computers via a search box and search submit button


  Background:
    Given I open a Chrome web browser


  @SEA01
  Scenario Outline: Users can search for computers
    Given I see the Computer Database home page
    When I enter "<search_phrase>" in the search box
    And I click the "search submit" button
    Then I should see the Computers Search Results page

  Examples:
    | search_phrase |
    | fake name     |
    | ACE           |

  @skip
  Scenario: Users search with an empty search box
    Given I see the Computer Database home page
    And the search box is empty
    When I click the "search submit" button
    Then I should see the Computers Search Results page
