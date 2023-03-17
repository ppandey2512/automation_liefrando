import pytest
from web.pages_objects import SearchPage, ResultPage 
from selenium.webdriver.common.by import By
from .config import setup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver


class Test_project:
    baseurl='https://www.lieferando.de/en/'

    def test_001(self, setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.SearchPage = SearchPage(setup)
        self.ResultPage = ResultPage(setup)
        self.SearchPage.click(self.SearchPage._ACCEPT_COOKIES)
        self.SearchPage.click(self.SearchPage._SEARCH_TEXTBOX)
        self.SearchPage.send_keys(self.SearchPage._SEARCH_TEXTBOX, 'Rhinstraße 133')
        self.SearchPage.click(self.SearchPage._SEARCH_SUGGESTION)
        self.ResultPage.click(self.ResultPage._MINIMUM_ORDER_VALUE_10)
        self.ResultPage.scroll_to_bottom()
        self.ResultPage.get_restaurants()
        minimum_order_value = self.ResultPage.min_order_values()
        if any(minimum_order_value) > 10:
            assert False
        assert True


    def test_002(self, setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.SearchPage = SearchPage(setup)
        self.ResultPage = ResultPage(setup)
        self.SearchPage.click(self.SearchPage._ACCEPT_COOKIES)
        self.SearchPage.click(self.SearchPage._SEARCH_TEXTBOX)
        self.SearchPage.send_keys(self.SearchPage._SEARCH_TEXTBOX, 'Rhinstraße 133')
        self.SearchPage.click(self.SearchPage._SEARCH_SUGGESTION)
        self.ResultPage.click(self.ResultPage._ITAIAN_CATEGORY)
        self.ResultPage.get_cuisines()

        assert 'Italian' in self.ResultPage.get_cuisines()