from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    def verify_search_results(self):
        expected_result = '"spf"'
        actual_result = self.driver.find_element(*self.RESULT_TEXT).text
        assert expected_result == actual_result,\
            f'Error! Expected {expected_result} bot got actual {actual_result}'