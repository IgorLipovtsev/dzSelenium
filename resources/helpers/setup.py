"""Модуль с методами работы драйвера"""
import pytest
import allure
import json

class BaseSetUp:

    @pytest.fixture(autouse=True)
    def set_up_driver(self, driver):
        self.driver = driver
        session_id = self.driver.session_id
        allure.attach(name=session_id,
                      body=json.dumps(self.driver.desired_capabilities),
                      attachment_type=allure.attachment_type.JSON)
        yield self.driver

    # def get_page(self, Page):
    #     return Page(self.driver)

    def check_console(self, driver):
        """Метод проверки корректности логов"""
        self.driver = driver
        for log in self.driver.get_log('browser'):
            assert 'Uncaught' not in log