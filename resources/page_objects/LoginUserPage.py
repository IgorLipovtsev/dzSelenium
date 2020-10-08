from resources.locators import Common
from resources.page_objects.common import BasePage
from fixtures.logger import browser_log

class LoginUserPage(BasePage):

    LOGGER_NAME = 'LoginUserPage'
    def __init__(self, driver):
        super().__init__(driver, logger_name=LoginUserPage.LOGGER_NAME)

    def login_user(self, email, password):
        self._click(Common.portal.account_menu)
        self._click(Common.portal.account_login)
        self._input(Common.portal.email, email)
        self._input(Common.portal.password, password)
        self._click(Common.portal.login)
        self.logger.info(f'{email} was logged in to Portal')
        return self

    def login_admin_user(self, username, password):
        self._navigate_to("http://192.168.64.2/admin/")
        self._input(Common.admin.username, username)
        self._input(Common.admin.password, password)
        self._click(Common.admin.login)
        self.logger.info(f'{username} was logged in to Admin tool')
        return self


    def navigate_to_homepage(self):
        self._navigate_to("http://192.168.64.2/")
        return self
