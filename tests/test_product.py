import pytest, os
from page_objects.common import UserPage
from page_objects import AdminToolPage


@pytest.fixture()
def password():
    os.chdir("/Users/lipa_/Desktop/QA_automation/dzSelenium/")
    with open("password", "r") as f:
        password = f.read()
    return password


@pytest.fixture()
def add_new_product(browser, password):
    """фикстура создания продукта"""
    UserPage(browser).login_admin_user("user", password)
    AdminToolPage(browser) \
        .open_catalog() \
        .open_products() \
        .add_new_product()
    name_of_product = "Ipad super 2020"
    AdminToolPage(browser) \
        .set_name_of_product(name_of_product) \
        .set_meta_tag_of_product("Ipad") \
        .set_data("premium") \
        .upload_new_image_avatar('/Users/lipa_/Desktop/Spider.jpg') \
        .save_product()
    return name_of_product


def test_delete_newly_added_product(browser, add_new_product):
    """удаляем только что добавленный продукт """
    AdminToolPage(browser).delete_newly_added_product(add_new_product)
    assert AdminToolPage(browser).check_count_of_products() == 20


def test_update_newly_added_product(browser, add_new_product):
    """обновляем description для только что добавленного продукта """

    AdminToolPage(browser) \
        .update_newly_added_product(add_new_product) \
        .set_description("some new info to update description") \
        .save_product()
    assert AdminToolPage(browser).check_count_of_products() == 21
