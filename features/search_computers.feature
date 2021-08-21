@search
Feature: Computers Database home page displays an action header, which allows users
  to search for computers via a search box and search submit button


  Background:
    Given I open a Chrome web browser
    And I see the Computer Database home page


  @skip
  @sanity
  @SEA01
  Scenario Outline: Search box is editable
    When I enter "<search_phrase>" into the search box
    Then I should see "<search_phrase>" in the search box

    Examples:
      | search_phrase |
      | fake name     |
      | ACE           |


  @sanity
  @SEA02
  Scenario: Search submit button is clickable
    Given I see the Computer Database home page
    When I click the "search submit" button
    Then I should see the Computers Search Results page


  @SEA03
  Scenario Outline: Users can search for computers
    Given I see the Computer Database home page
    When I enter "<search_phrase>" in the search box
    And I click the "search submit" button
    Then I should see the Computers Search Results page

  Examples:
    | search_phrase |
    | fake name     |
    | ACE           |


  @SEA04
  Scenario: Users search with an empty search box
    Given I see the Computer Database home page
    And the search box is empty
    When I click the "search submit" button
    Then I should see the Computers Search Results page


  @SEA05
  # Note: this scenario depends on preloaded data existing on the target environment
  Scenario Outline: Searching for computers yields results
    Given I see the Computer Database home page
    When I enter "<search_phrase>" in the search box
    And I click the "search submit" button
    Then I should see the Computers Search Results page
    And I should see at least 1 result

    Examples:
      | search_phrase |
      | A             |
