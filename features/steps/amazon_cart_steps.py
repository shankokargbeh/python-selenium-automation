from behave import given, when, then
from selenium.webdriver.common.by import By




@given("Open Amazon Page")
def step_impl(context):
    context.driver.get("https://www.amazon.com")

@when("Search for Product")
def search_product(context):
    search_bar = context.driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
    search_bar.send_keys("iPhone 14 Pro Max")

@when("click on  the Search Icon")
def click_on_search(context):
    search_icon = context.driver.find_element(By.XPATH, '//span[@id="nav-search-submit-text"]')
    search_icon.click()

@when("click on the first product")
def click_on_the_first_product(context):
    search_product = context.driver.find_element(By.XPATH, '//span[@class="a-price-whole"]')
    search_product.click()
@when("add product to cart")
def add_product_to_cart(context):
    add_product = context.driver.find_element(By.XPATH, '//input[@id="submit.add-to-cart"]')
    add_product.click()


@then("verify item in cart")
def verify_cart_count(context):
    expected_cart_count = "1"
    cart_count = context.driver.find_element(By.XPATH, '//span[@id="nav-cart-count"]').text
    assert expected_cart_count == cart_count, f'Expected {expected_cart_count} but got {cart_count}'

