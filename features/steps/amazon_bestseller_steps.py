from behave import *
from selenium.webdriver.common.by import By


@given("Open Amazon Bestsellers Page")
def step_impl(context):
   context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then("Verify that there are  5 links")
def step_impl(context):
    actual_links = context.driver.find_elements(By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']//a")
    assert len(actual_links) == 5, f"Expected links not found"