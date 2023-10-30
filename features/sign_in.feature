Feature: sign_in functionality
  As a user I want to login to appication

  Scenario Outline: Log in with valid data
    Given User opens the main page
    When user clicks on the button: "Hello,sign in"
    And user fills in valid <email> and <password>
    Then user should be logged in to application
    Examples:
    |email | password |
    |7799298050         | shonu@556 |

  Scenario Outline: Log in with invalid data
    Given user opens the main page
    When user clicks on the button: "Hello,sign in"
    And user fills in invalid <email>
    Then user should not be logged in to application
    Examples:
      |email | password |
      |77992980501        | shonu@556 |