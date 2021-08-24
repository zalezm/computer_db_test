@delete
@skip
Feature: Users can delete an existing computer from the Edit Computer page. Deleting a computer entry removes it
  from the portal immediately, informing users of successful delete operations.


  Background:
    Given I open a Chrome web browser


  @DEL01
  Scenario: Users can delete an existing computer entry
    Given computer with name "Test PC Name 1x2y3z" exists
    And I see the Computers Search Results page
    And I click on Computers table entry with name "Test PC Name 1x2y3z"
    And I see the Edit Computers page
    When I click on the "delete this computer" button
    Then I should see the Computer Database home page
    And the Computer Database home page should display the "Delete success" banner
    When I search for for "Test PC Name 1x2y3z"
    Then I should see the Computers Search Results page
    And I should not see any results

  @DEL02
  Scenario: Deleted computers are removed permanently
    Given computer with name "Test PC Name 1x2y3z" exists
    And I navigate to the Edit Computers page for computer with name "Test PC Name 1x2y3z"
    And I capture the computer ID from the URL
    And I delete computer with name "Test PC Name 1x2y3z"
    When I load to the Computer Edit page URL for the captured computer ID
    Then I should get a 404 Response
