from locators import Common
from page_objects import BasePage


class UserPage(BasePage):

    def login_user(self, email, password):
        self._click(Common.portal.account_menu)
        self._click(Common.portal.account_login)
        self._input(Common.portal.email, email)
        self._input(Common.portal.password, password)
        self._click(Common.portal.login)
        return self

    def login_admin_user(self, username, password):
        self._navigate_to("http://192.168.64.2/admin/")
        self._input(Common.admin.username, username)
        self._input(Common.admin.password, password)
        self._click(Common.admin.login)
        return self

    def navigate_to_homepage(self):
        self._navigate_to("http://192.168.64.2/")
        return self
