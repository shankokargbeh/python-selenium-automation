from behave import *

use_step_matcher("re")


@given("Open Main Page")
def step_impl(context):
    context.app.main_page.open_main_page()


@when("Click search button")
def click_search_btn(context):
    context.app.header.search_for_product()

@then('Verify search results shown')
def verify_search_results(context):
    context.app.search_results_page.verify_search_results()



