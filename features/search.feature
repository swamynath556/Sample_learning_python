Feature:  Search functionality of the application
  As a user I want to verify the search functionality of the application

  @home
  Scenario: Check if search bar is working fine.
    Given User opens the main page
    When User searches with value : "iqoo 9t"
    Then User should get results related to "iqoo 9t"
