from behave import given, when, then


@when('Click on “off plan” at the left side menu.')
def click_off_plan(context):
    context.app.off_plan_page.click_off_plan()


@then('Verify the right page opens.')
def verify_off_plan_opens(context):
    context.app.off_plan_page.verify_off_plan_opens()


@when('Filter by sale status of “High Demand”.')
def filter_projects(context):
    context.app.off_plan_page.filter_projects()


@then('Verify each product contains the High Demand tag.')
def filter_projects(context):
    context.app.off_plan_page.verify_high_demand_project_tag()


@then('Filter the products by price range from 1200000 to 2000000 AED.')
def filter_project_price(context):
    context.app.off_plan_page.filter_project_price()


@then('Verify the price in all cards is inside the range (1200000 - 2000000).')
def verify_project_price(context):
    context.app.off_plan_page.verify_project_price()