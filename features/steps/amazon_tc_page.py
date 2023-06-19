from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC




@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/')

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
