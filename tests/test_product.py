import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import AdminTool


@pytest.fixture()
def password():
    os.chdir("/Users/lipa_/Desktop/QA_automation/dzSelenium/")
    with open("password", "r") as f:
        password = f.read()
    return password


@pytest.fixture()
def add_new_product(browser, url_setup, password):
    """добавляем новый продукт """

    wait = WebDriverWait(browser, 10)
    browser.get(url_setup)
    browser.find_element(*AdminTool.username).send_keys("user")
    browser.find_element(*AdminTool.password).send_keys(password)
    browser.find_element(*AdminTool.login).click()
    wait.until(EC.presence_of_element_located(AdminTool.catalog)).click()
    browser.find_element(*AdminTool.products).click()
    count_of_products = browser.find_elements(*AdminTool.list_of_products)
    browser.find_element(*AdminTool.add_new_product).click()
    browser.find_element(*AdminTool.data).click()
    browser.find_element(*AdminTool.model).send_keys("budjet")
    browser.find_element(*AdminTool.general).click()
    name_of_new_product = "Iphone 11 Super Pro Max XXL"
    browser.find_element(*AdminTool.product_name).send_keys(f"{name_of_new_product}")
    browser.find_element(*AdminTool.meta_tag_title).send_keys("super iphone")
    browser.find_element(*AdminTool.image).click()
    browser.find_element(*AdminTool.default_image).click()

    wait.until(EC.presence_of_element_located(AdminTool.image_manager)).click()
    wait.until(EC.presence_of_element_located(AdminTool.image_upload))
    browser.execute_script("$('#button-upload').click();")
    file = browser.find_element(*AdminTool.file_upload)
    file.send_keys('/Users/lipa_/Desktop/Spider.jpg')
    wait.until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()
    wait.until(EC.presence_of_element_located(AdminTool.image_upload))
    wait.until(EC.presence_of_element_located(AdminTool.new_avatar)).click()
    wait.until(EC.presence_of_element_located(AdminTool.save_product)).click()

    return name_of_new_product


def test_delete_newly_added_product(browser, url_setup, add_new_product, password):
    """удаляем только что добавленный продукт """

    wait = WebDriverWait(browser, 10)
    browser.get(url_setup)
    browser.find_element(*AdminTool.username).send_keys("user")
    browser.find_element(*AdminTool.password).send_keys(password)
    browser.find_element(*AdminTool.login).click()
    wait.until(EC.presence_of_element_located(AdminTool.catalog)).click()
    browser.find_element(*AdminTool.products).click()

    count_of_products = browser.find_elements(*AdminTool.list_of_products)

    newly_added_product = browser.find_element_by_xpath(
        f"//*[contains(text(), '{add_new_product}')]"
    )
    # newly_added_product_checkbox = browser.find_element_by_xpath(f"//*[text() = '{add_new_product}']/parent::tr//input")

    xpath_all_products = browser.find_elements(*AdminTool.add_checkbox_to_product)

    product_position = 0
    for product in count_of_products:
        if newly_added_product.location["y"] == product.location["y"]:
            xpath_all_products[product_position].click()
        product_position = product_position + 1

    browser.find_element(*AdminTool.delete_product).click()
    alert = browser.switch_to.alert
    alert.accept()
    count_of_products = browser.find_elements(*AdminTool.list_of_products)
    assert len(count_of_products) == 20


def test_update_newly_added_product(browser, url_setup, add_new_product, password):
    """обновляем description для только что добавленного продукта """

    wait = WebDriverWait(browser, 10)
    browser.get(url_setup)
    browser.find_element(*AdminTool.username).send_keys("user")
    browser.find_element(*AdminTool.password).send_keys(password)
    browser.find_element(*AdminTool.login).click()
    wait.until(EC.presence_of_element_located(AdminTool.catalog)).click()
    browser.find_element(*AdminTool.products).click()

    count_of_products = browser.find_elements(*AdminTool.list_of_products)

    newly_added_product = browser.find_element_by_xpath(
        f"//*[contains(text(), '{add_new_product}')]"
    )
    newly_added_product_edit = browser.find_element_by_xpath(
        f"//*[text() = '{add_new_product}']/parent::tr//*[contains(@class,'btn btn-primary')]"
    ).click()

    browser.find_element(*AdminTool.description).send_keys(
        "some new info to update description"
    )
    browser.find_element(*AdminTool.save_product).click()
    wait.until(EC.presence_of_element_located(AdminTool.alert_success))
    browser.find_element(*AdminTool.alert_success_close).click()

    count_of_products = browser.find_elements(*AdminTool.list_of_products)
    assert len(count_of_products) == 21
