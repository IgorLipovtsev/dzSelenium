from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import logging
from .logger import browser_log
import os


class BrowserListener(AbstractEventListener):
    """Класс для работы с событиями в браузере"""

    def on_exception(self, exception, driver):
        """Метод снятия скриншота при возникновении ошибки"""
        logging.error(f'{exception}')
        current_path = os.getcwd()
        os.chdir(f"{current_path}/screenshots/")
        driver.save_screenshot(f'{exception}.png')


class Browser:
    """Класс для работы с настройками браузеров"""

    LOGGER_NAME = 'browser'

    def __init__(self, browser, wait):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            self.driver = EventFiringWebDriver(webdriver.Chrome(options=options), BrowserListener())
        elif browser == "firefox":
            self.driver = EventFiringWebDriver(webdriver.Firefox(), BrowserListener())
        elif browser == "opera":
            self.driver = EventFiringWebDriver(webdriver.Opera(), BrowserListener())
        elif browser == "safari":
            self.driver = EventFiringWebDriver(webdriver.Safari(), BrowserListener())
        else:
            raise Exception(f"This browser is not supported!")

        self.driver.maximize_window()
        self.driver.implicitly_wait(wait)
        self.browser_log = browser_log(self.LOGGER_NAME)

#     elif browser == "Firefox":
#         driver = EventFiringWebDriver(webdriver.Firefox(), BrowserListener())
#     elif browser == "Opera":
#         driver = EventFiringWebDriver(webdriver.Opera(), BrowserListener())
#     elif browser == "Safari":
#         driver = EventFiringWebDriver(webdriver.Safari(), BrowserListener())
#     else:
#         raise Exception(f"This browser is not supported!")
#
#     driver.maximize_window()
#     driver.implicitly_wait(implicitly_wait_value)
#     logger.info("Browser started!")
#
#     # def fin():
#     #     driver.quit()
#     #     driver.info("Browser closed")
#     #     driver.info(f"Test {test_name} finished")
#     request.addfinalizer(driver.quit)
#
#     # driver.maximize_window()
#     # driver.implicitly_wait(implicitly_wait_value)
#     return driver
