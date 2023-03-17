from .basepage import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    _SEARCH_TEXTBOX = (By.NAME, "searchText")
    _SEARCH_BUTTON = (By.XPATH, '//button[@data-qa="location-panel-search-button"]')
    _ACCEPT_COOKIES= (By.XPATH,'//button[@aria-label="Accept all cookies"]')
    _SEARCH_SUGGESTION= (By.XPATH, '//li[@data-qa="location-panel-results-item-element"]')

   
    
    def __init__(self,driver):
        super().__init__(driver)
