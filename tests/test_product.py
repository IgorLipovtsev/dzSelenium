import pytest
import os
import allure
from selenium.common.exceptions import NoSuchElementException
from resources.page_objects import LoginUserPage
from resources.page_objects import AdminToolPage
from resources.helpers.setup import BaseSetUp


# def test_delete_newly_added_product(driver, add_new_product):
#     """удаляем только что добавленный продукт """
#     AdminToolPage(driver).delete_newly_added_product(add_new_product)
#     assert AdminToolPage(driver).check_count_of_products() == 20
#     # driver.save_screenshot('finish_test.png')
#


class TestProducts(BaseSetUp):

    @pytest.fixture()
    def password(self):
        os.chdir("/Users/lipa_/Desktop/QA_automation/dzSelenium/")
        with open("password", "r") as f:
            password = f.read()
        self.check_console(self.driver)
        return password

    @pytest.fixture()
    def add_new_product(self, password):
        """фикстура создания продукта"""
        LoginUserPage(self.driver).login_admin_user("user", password)
        AdminToolPage(self.driver) \
            .open_catalog() \
            .open_products() \
            .add_new_product()
        name_of_product = "Ipad super 2020"
        AdminToolPage(self.driver) \
            .set_name_of_product(name_of_product) \
            .set_meta_tag_of_product("Ipad") \
            .set_data("premium") \
            .upload_new_image_avatar('/Users/lipa_/Desktop/Spider.jpg') \
            .save_product()
        self.check_console(self.driver)
        return name_of_product


    @allure.feature('Admin Tool')
    @allure.story('Working with Product')
    @allure.title('Delete Product')
    def test_delete_newly_added_product(self, add_new_product):
        """удаляем только что добавленный продукт """
        AdminToolPage(self.driver).delete_newly_added_product(add_new_product)
        assert AdminToolPage(self.driver).check_count_of_products() == 20
        # self.driver.save_screenshot('finish_test.png')
        self.check_console(self.driver)

    # @allure.feature('Admin Tool')
    # @allure.story('Working with Product')
    # @allure.title('Update description for Product')
    # def test_update_newly_added_product(self, add_new_product):
    #     """обновляем description для только что добавленного продукта """
    #
    #     AdminToolPage(self.driver) \
    #         .update_newly_added_product(add_new_product) \
    #         .set_description("some new info to update description") \
    #         .save_product()
    #
    #     assert AdminToolPage(self.driver).check_count_of_products() == 21
