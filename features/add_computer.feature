@add
Feature: Users can add a computer by clicking the add button on the main portal
  and entering all required fields and any optional fields

  Background:
    Given I open a Chrome web browser


  @sanity
  @ADD01
  Scenario: Add Computer page is visible
    Given I see the Computer Database home page
    When I click the "add a new computer" button
    Then I should see the Add Computer page


  @ADD02
  @skip
  Scenario Outline: Adding a computer without required fields fails
    Given I load the Add Computer page into the web browser
    And I see the Add Computer page
    When I leave required field "<required_field>" empty
    And I click the "create this computer" button
    Then I should see the Add Computer page
    And required field "<required_field>" should be highlighted

  Examples:
  | required_field |
  | Computer name  |


  @ADD03
  @skip
  Scenario Outline: Adding a computer with invalid optional fields fail
    Given I load the Add Computer page into the web browser
    And I see the Add Computer page
    When I enter required field values:
      | required_field | required_field_value |
      | Computer name  | Test PC Name A1B2C3  |
    And I enter optional field "<optional_field>" value "<optional_field_value>"
    And I click "create this computer" button
    Then I should see the Add Computer page
    And optional field "<optional_field>" should be highlighted

  Examples:
  | optional_field    | optional_field_value |
  | Introduced date   | ABCDEFGHIJ           |
  | Discontinued date | ABCDEFGHIJ           |


  @ADD04
  @skip
  Scenario: Users can add a new computer with all required fields only
    Given I load the Add Computer page into the web browser
    And I see the Add Computer page
    When I enter the following required field values:
      | required_field | required_field_value |
      | Computer name  | Test PC Name A1B2C3  |
    And I click "create this computer" button
    Then I should see the Computer Database home page
    And the Computer Database home page should display the "Add success" banner
    When I search for computer name "Test PC Name A1B2C3"
    Then I should see the Computers Search Results page
    # note: this step checks for 1+ result in case cleanup steps fail to remove all instances of test data
    And I should see at least 1 result


  @ADD05
  @skip
  Scenario: Users can add a new computer with all required fields and optional fields
    Given I load the Add Computer page into the web browser
    And I see the Add Computer page
    When I enter required field values:
      | required_field | required_field_value |
      | Computer name  | Test PC Name C4D5E6  |
    And I enter optional field values:
      | optional_field    | optional_field_value |
      | Introduced date   | 2021-01-01           |
      | Discontinued date | 2021-02-02           |
      | Company           | IBM                  |
    And I click "create this computer" button
    Then I should see the Computer Database home page
    And the Computer Database home page should display the "Add success" banner
    When I search for computer name "Test PC Name C4D5E6"
    Then I should see the Computers Search Results page
    # note: this step checks for 1+ result in case cleanup steps fail to remove all instances of test data
    And I should see at least 1 result


  @ADD06
  @skip
  Scenario: Users can cancel adding a new computer
    Given I load the Add Computer page into the web browser
    And I see the Add Computer page
    When I enter required field values:
      | required_field | required_field_value |
      | Computer name  | Test PC Name 9Z8Y7X  |
    And I enter optional field values:
      | optional_field    | optional_field_value |
      | Introduced date   | 2021-01-01           |
      | Discontinued date | 2021-02-02           |
      | Company           | IBM                  |
    And I click "create this computer" button
    Then I should see the Computer Database home page
    And the Computer Database home page should not display the "Add success" banner
    When I search for computer name "Test PC Name 9Z8Y7X"
    Then I should see the Computers Search Results page
    And I should not see any results
