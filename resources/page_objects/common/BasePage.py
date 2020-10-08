from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.logger import browser_log


class BasePage:
    LOGGER_NAME = 'base'

    def __init__(self, driver, logger_name=LOGGER_NAME):
        self.logger = browser_log(logger_name)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def __element(self, by: str, selector: str):
        try:
            self.wait.until(EC.presence_of_element_located((by, selector)))
            self.wait.until(EC.element_to_be_clickable((by, selector)))
        except:
            raise self.logger.error(Exception(f'Element {(by, selector)} is NOT found!'))
            # raise self.logger.error(NoSuchElementException(f'Element {(by, selector)} is NOT found!'))

        self.logger.info(f'Element {(by, selector)}  found')
        return self.driver.find_element(by, selector)

    def _click(self, selector):
        try:
            self.__element(selector[0], selector[1]).click()
        except:
            raise self.logger.error(Exception(f'Element {(selector[0], selector[1])} can NOT be clicked!'))
        self.logger.info(f'Element {selector[0], selector[1]} can be clicked')

    def _input(self, selector, value):
        try:
            self.__element(selector[0], selector[1]).clear()
            self.__element(selector[0], selector[1]).send_keys(value)
        except:
            raise self.logger.error(
                Exception(f'Element {(selector[0], selector[1])}  can NOT be used for input data!'))
        self.logger.info(f'Element {(selector[0], selector[1])} can be used for input data')

    def _wait_for_visible(self, selector, wait=10):
        # self.logger.info(f'Element {(selector[0], selector[1])} is visible in DOM')
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector[0], selector[1])))

    def _navigate_to(self, url):
        self.driver.get(url)
