from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")
#POPUP_SIGNIN_BTN = (By.XPATH, "//div[@id='nav-signin-tooltip']/a")

@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.driver.find_element(*SEARCH_FILED).send_keys(search_query)
    context.driver.find_element(*SEARCH_BTN).click()

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()
    element = context.driver.find_element(*ORDERS_BTN)
    print('Before refresh: ', element)
    context.driver.refresh()
    element = context.driver.find_element(*ORDERS_BTN)
    print('After refresh: ', element)
    element.click()


@when('Verify Orders btn present')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN)

@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    ).click()

@then('Verify Sign In is clickable')
def verify_signin_popup_btn_clickable(context):
    context.driver.wait.until(EC.presence_of_element_located(POPUP_SIGNIN_BTN),message='Signin btn not clickable')

@then('Verify Sign In disappears')
def verify_signin_popup_btn_disappears(context):
    context.driver.wait.until(
     EC.invisibility_of_element_located(POPUP_SIGNIN_BTN),
     message='Signin btn did not disappear'
     )



#@then('Verify Sign In is clickable')
#def verify_signin_popup_btn_clickable(context):
#    context.driver.wait.until(
#        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
#        message='Signin btn not clickable'
#    )


#@then('Verify Sign In disappears')
#def verify_signin_popup_btn_disappears(context):
#    context.driver.wait.until(
#        EC.invisibility_of_element_located(POPUP_SIGNIN_BTN),
#        message='Signin btn did not disappear'
#    )

@when('Wait for {sec_amount} sec')
def wait_sec(context, sec_amount):
    sleep(int(sec_amount))


#@then('Verify Sign In is clickable')
#def verify_signin_popup_btn_clickable(context):
##    context.driver.wait.until(
#        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
#        message='Signin btn not clickable'
#    )


#@then('Verify Sign In disappears')
#def verify_signin_popup_disappears(context):
#    context.driver.wait.until_not(
#        EC.visibility_of_element_located(POPUP_SIGNIN_BTN),
#        message='Signin btn did not disappear'
#    )


@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)

