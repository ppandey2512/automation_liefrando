from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    """ Wrapper for selenium operations """

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 180)

    def click(self, webelement) -> None:
        el: WebElement = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.click()

    def fill_text(self, webelement, txt: str) -> None:
        el: WebElement = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()
        el.send_keys(txt)

    def send_keys(self, webelement,key) -> None:
        el: WebElement = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.send_keys(key)

    def scroll_to_bottom(self) -> None:
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_elem_displayed(self, webelement) -> bool:
        try:
            return webelement.is_displayed()
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False

    def find_elements(self, webelement) -> WebElement:
        return self._driver.find_elements(*webelement)

    def find_element(self, webelement) -> WebElement:
        return self._driver.find_element(*webelement)