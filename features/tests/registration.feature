Feature: Test scenarios for registration page

  @smoke
  Scenario: The user can enter the information into the input fields on the registration page
    Given Open the main page
    When Enter some test information in the input fields.
    Then Verify the right information is present.