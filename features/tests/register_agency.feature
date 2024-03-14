Feature: Test Scenarios to connect the company

  Scenario: User clicks on “Connect the company” button and can use the form to register a new agency
    Given Open the main page
    When Click on the sign in
    When Log in to the page.
    And Click on "Connect the company".
    And Switch the new tab
    And Enter some test information in the form
    Then Verify the right information is present
    And Verify "send request" button is available and clickable
    And Verify "buy a subscription" button is available and clickable