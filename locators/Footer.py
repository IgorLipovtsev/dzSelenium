from selenium.webdriver.common.by import By


class Footer:
    # INFORMATION
    about_us = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(1) > .list-unstyled  li:nth-child(1) a",
    )
    delivery_infromation = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(1) > .list-unstyled  li:nth-child(2) a",
    )
    privacy_pilicy = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(1) > .list-unstyled  li:nth-child(3) a",
    )
    terms_and_conditions = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(1) > .list-unstyled  li:nth-child(4) a",
    )

    # CUSTOMER SERVICE
    contact_us = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(2) > .list-unstyled  li:nth-child(1) a",
    )
    returns = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(2) > .list-unstyled  li:nth-child(2) a",
    )
    site_map = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(2) > .list-unstyled  li:nth-child(3) a",
    )

    # EXTRAS
    brands = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(3) > .list-unstyled  li:nth-child(1) a",
    )
    gift_certificates = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(3) > .list-unstyled  li:nth-child(2) a",
    )
    affiliate = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(3) > .list-unstyled  li:nth-child(3) a",
    )
    specials = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(3) > .list-unstyled  li:nth-child(4) a",
    )

    # MY ACCOUNT
    my_account = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(4) > .list-unstyled  li:nth-child(1) a",
    )
    order_history = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(4) > .list-unstyled  li:nth-child(2) a",
    )
    wish_list = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(4) > .list-unstyled  li:nth-child(3) a",
    )
    newsletter = (
        By.CSS_SELECTOR,
        ".col-sm-3:nth-child(4) > .list-unstyled  li:nth-child(4) a",
    )
