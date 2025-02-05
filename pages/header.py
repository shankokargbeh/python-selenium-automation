from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    def search_for_product(self):
        self.input_text('spf', *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)
