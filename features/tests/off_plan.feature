Feature: Features of off-plan page


  Scenario: User can filter by sale status High Demand
    Given Open the main page
    When Click on the sign in
    When Log in to the page.
    And Click on “off plan” at the left side menu.
    Then Verify the right page opens.
    When Filter by sale status of “High Demand”.
    Then Verify each product contains the High Demand tag.

  @smoke
  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page
    When Click on the sign in
    When Log in to the page.
    And Click on “off plan” at the left side menu.
    Then Verify the right page opens.
    And Filter the products by price range from 1200000 to 2000000 AED.
    And Verify the price in all cards is inside the range (1200000 - 2000000).
