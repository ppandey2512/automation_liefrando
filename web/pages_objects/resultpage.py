from .basepage import BasePage
from selenium.webdriver.common.by import By


class ResultPage(BasePage):


    _MINIMUM_ORDER_VALUE_10 = (By.XPATH, './/input[@value="1000" and @data-qa="radio-element"]/..')
    _ITAIAN_CATEGORY = (By.XPATH, '//div[@aria-label="Select Italian category"]')
    _RESTAURANTS = (By.XPATH, '//div[@data-qa="mov-indicator-content"]')
    _RESTAURANT_HEADER = (By.XPATH, '//h1[@data-qa="restaurant-list-header"]')

    def __init__(self,driver):
        super().__init__(driver)

    def get_restaurants(self):
        return self.find_elements(self._RESTAURANTS)


    def min_order_values(self):
        return [self.clean_mov(Y.text) for Y in [*self.get_restaurants()]]


    def clean_mov(self,mov_text):
        mov_eur, mov_cents = mov_text.replace('€', '').replace('Min. ','').strip().split(',')
        return int(mov_eur) + int(mov_cents) / 100

    def get_cuisines(self):
        return self.find_element(self._RESTAURANT_HEADER).text