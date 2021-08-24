@edit
@skip
Feature: Users can edit existing computers, updating any fields so long as required fields are present. Users
  can persist changes made on the computer edit page or cancel changes.

  Background:
    Given I open a Chrome web browser


  @EDI01
  Scenario: Users can view the edit page for a computer entry
    Given computer with name "Test PC Name 1a2b3c" exists
    And I see the Computers Search Results page
    When I click on Computers table entry with name "Test PC Name 1a2b3c"
    Then I should see the Edit Computers page

  @EDI02
  Scenario: Users can edit required fields for an existing computer entry
    Given computer with name "Test PC Name 1a2b3c" exists
    And computer with name "Test PC Name a1b2c3" does not exist
    And I navigate to the Edit Computers page for computer with name "Test PC Name 1a2b3c"
    And I enter required field values:
      | required_field | required_field_value |
      | Computer name  | Test PC Name a1b2c3  |
    When I click "save this computer" button
    Then I should see the Computer Database home page
    And the Computer Database home page should display the "Edit success" banner

  @EDI03
  Scenario: Users can edit optional fields for an existing computer entry
    Given computer with name "Test PC Name 1a2b3c" exists
    And computer with name "Test PC Name a1b2c3" does not exist
    And I navigate to the Edit Computers page for computer with name "Test PC Name 1a2b3c"
    And I enter optional field values:
      | optional_field    | optional_field_value |
      | Introduced date   | 2021-01-01           |
      | Discontinued date | 2021-02-02           |
      | Company           | RCA                  |
    When I click "save this computer" button
    Then I should see the Computer Database home page
    And the Computer Database home page should display the "Edit success" banner
