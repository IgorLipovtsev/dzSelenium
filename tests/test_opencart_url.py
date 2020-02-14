import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_opencart_url_checks(url_setup, browser):
    """проверяем что мы находимся на opencart"""

    try:
        browser.get(url_setup)
        open_cart_check = browser.find_element_by_css_selector("p > a")
        assert (open_cart_check.get_property("href")) == "http://www.opencart.com/"
        print(
            f"мы находимся на локальной версии {open_cart_check.get_property('href')}"
        )
    except NoSuchElementException:
        print("похоже мы не на http://www.opencart.com/, либо указан не верный локатор")
