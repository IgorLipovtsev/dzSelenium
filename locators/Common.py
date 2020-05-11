from selenium.webdriver.common.by import By


class Common:
    class admin:
        # login to admin tool
        username = (By.CSS_SELECTOR, 'input[name="username"]')
        password = (By.CSS_SELECTOR, 'input[name="password"]')
        forgot_password = (By.CSS_SELECTOR, '.help-block a')
        login = (By.CSS_SELECTOR, '.text-right button')

    class portal:
        # ACCOUNT
        account_menu = (By.CSS_SELECTOR, ".dropdown .fa")
        account_register = (By.CSS_SELECTOR, ".dropdown-menu.dropdown-menu-right li:nth-child(1) a")
        account_login = (By.CSS_SELECTOR, ".dropdown-menu.dropdown-menu-right li:nth-child(2) a")
        # login to admin tool
        email = (By.CSS_SELECTOR, "#input-email")
        password = (By.CSS_SELECTOR, "#input-password")
        forgot_password = (By.CSS_SELECTOR, '.form-group a')
        login = (By.CSS_SELECTOR, '.btn.btn-primary[value="Login"]')
