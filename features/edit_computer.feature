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
