from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, by: str, selector: str, index: int):
        return self.driver.find_elements(by, selector)[index]

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector[0], selector[1], index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector[0], selector[1], index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, index=0, wait=5):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector[0], selector[1], index)))

    def _navigate_to(self, url):
        self.driver.get(url)
