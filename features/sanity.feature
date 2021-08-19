@sanity
Feature: Computer Database Portal is reachable via web browser and displays default web content


  Background:
    Given I open a Chrome web browser


  @SAN01
  Scenario: Loading Computer Database URL in a browser takes me to the home page
    When I load the Computer Database Portal into the web browser
    Then I should see the Computer Database home page URL


  @SAN02
  Scenario: Visiting the Computer Databasae Portal
    When I load the Computer Database Portal into the web browser
    Then I should see the Computer Database home page