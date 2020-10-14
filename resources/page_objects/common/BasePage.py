from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from fixtures.logger import browser_log
import allure


class BasePage:
    LOGGER_NAME = 'base'

    def __init__(self, driver, logger_name=LOGGER_NAME):
        self.logger = browser_log(logger_name)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def __element(self, by: str, selector: str):
        with allure.step(f"проверяем наличие {selector} на странице"):
            try:
                self.wait.until(EC.presence_of_element_located((by, selector)))
                self.wait.until(EC.element_to_be_clickable((by, selector)))
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                self.logger.error(f'Element {(by, selector)} is NOT found!')
                raise AssertionError
            # raise self.logger.error(NoSuchElementException(f'Element {(by, selector)} is NOT found!'))

        self.logger.info(f'Element {(by, selector)}  found')
        return self.driver.find_element(by, selector)

    def _click(self, selector):
        with allure.step(f"выполняем клик по {selector}"):
            try:
                self.__element(selector[0], selector[1]).click()
            except TimeoutException:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                self.logger.error(f'Element {(selector[0], selector[1])} can NOT be clicked!')
                raise AssertionError

        self.logger.info(f'Element {selector[0], selector[1]} can be clicked')

    def _input(self, selector, value):
        with allure.step(f"вводим значение {value} в поле и делаем клик по {selector}"):
            self.__element(selector[0], selector[1]).clear()
            self.__element(selector[0], selector[1]).send_keys(value)
            self.logger.info(f'Element {(selector[0], selector[1])} can be used for input data')

    def _wait_for_visible(self, selector, wait=10):
        # self.logger.info(f'Element {(selector[0], selector[1])} is visible in DOM')
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector[0], selector[1])))

    def _navigate_to(self, url):
        self.driver.get(url)
