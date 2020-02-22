from selenium.webdriver.common.by import By


class Footer:
    # INFORMATION
    information = ".col-sm-3:nth-child(1) > .list-unstyled li:nth-child"
    about_us = (By.CSS_SELECTOR, f"{information}(1) a")
    delivery_infromation = (By.CSS_SELECTOR, f"{information}(2) a")
    privacy_pilicy = (By.CSS_SELECTOR, f"{information}(3) a")
    terms_and_conditions = (By.CSS_SELECTOR, f"{information}(4) a")

    # CUSTOMER SERVICE
    customer_service = ".col-sm-3:nth-child(2) > .list-unstyled  li:nth-child"
    contact_us = (By.CSS_SELECTOR, f"{customer_service}(1) a")
    returns = (By.CSS_SELECTOR, f"{customer_service}(2) a")
    site_map = (By.CSS_SELECTOR, f"{customer_service}(3) a")

    # EXTRAS
    extras = ".col-sm-3:nth-child(3) > .list-unstyled  li:nth-child"
    brands = (By.CSS_SELECTOR, f"{extras}(1) a")
    gift_certificates = (By.CSS_SELECTOR, f"{extras}(2) a")
    affiliate = (By.CSS_SELECTOR, f"{extras}(3) a")
    specials = (By.CSS_SELECTOR, f"{extras}(4) a")

    # MY ACCOUNT
    account = ".col-sm-3:nth-child(4) > .list-unstyled  li:nth-child"
    my_account = (By.CSS_SELECTOR, f"{account}(1) a")
    order_history = (By.CSS_SELECTOR, f"{account}(2) a")
    wish_list = (By.CSS_SELECTOR, f"{account}(3) a")
    newsletter = (By.CSS_SELECTOR, f"{account}(4) a")
