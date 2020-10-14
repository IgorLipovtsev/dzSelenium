import allure
from resources.locators import AdminTool
from resources.page_objects.common import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class AdminToolPage(BasePage):
    LOGGER_NAME = 'AdminToolPage'

    def __init__(self, driver):
        super().__init__(driver, logger_name=AdminToolPage.LOGGER_NAME)

    def open_catalog(self):
        with allure.step(f"открываем каталог"):
            self._wait_for_visible(AdminTool.catalog)
            self._click(AdminTool.catalog)
            return self

    def open_products(self):
        with allure.step(f"открываем продукты"):
            self._wait_for_visible(AdminTool.products)
            self._click(AdminTool.products)
            return self

    def check_count_of_products(self):
        with allure.step(f"измеряем количество продуктов"):
            count_of_products = self.driver.find_elements(*AdminTool.list_of_products)
            return len(count_of_products)

    def add_new_product(self):
        with allure.step(f"добавляем новый продукт"):
            self._wait_for_visible(AdminTool.add_new_product)
            self._click(AdminTool.add_new_product)
            self.logger.info(f'new product was successfully added!')
            return self

    def edit_product(self):
        with allure.step(f"делаем изменения для продукта"):
            self._wait_for_visible(AdminTool.add_new_product)
            self._click(AdminTool.add_new_product)
            self.logger.info(f'new product was successfully edited!')
            return self

    # product creation options
    def set_data(self, model):
        with allure.step(f"заполняем параметр {model}"):
            self._wait_for_visible(AdminTool.data)
            self._click(AdminTool.data)
            self._input(AdminTool.model, model)
            return self

    def set_description(self, description):
        with allure.step(f"заполняем параметр {description}"):
            self._wait_for_visible(AdminTool.description)
            self._click(AdminTool.description)
            self._input(AdminTool.description, description)
            self.logger.info(f'description was successfully changed!')
            return self

    def set_name_of_product(self, name_of_product):
        with allure.step(f"заполняем параметр {name_of_product}"):
            self._wait_for_visible(AdminTool.general)
            self._click(AdminTool.general)
            self._input(AdminTool.product_name, name_of_product)
            self.logger.info(f'name of product was successfully changed!')
            return self

    def delete_newly_added_product(self, newly_added_product):
        with allure.step(f"удаляем только что добавленный продукт {newly_added_product}"):
            element = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{newly_added_product}')]")
            count_of_products = self.driver.find_elements(*AdminTool.list_of_products)
            xpath_all_products = self.driver.find_elements(*AdminTool.add_checkbox_to_product)

            product_position = 0
            for product in count_of_products:
                if element.location["y"] == product.location["y"]:
                    xpath_all_products[product_position].click()
                product_position = product_position + 1

            self._wait_for_visible(AdminTool.delete_product)
            self._click(AdminTool.delete_product)
            Alert(self.driver).accept()
            self.logger.info(f'{newly_added_product} was successfully deleted!')
            return self

    def update_newly_added_product(self, add_new_product):
        with allure.step(f" обновляем только что добавленный {add_new_product}"):
            newly_added_element = (
            By.XPATH, f"//*[text() = '{add_new_product}']/parent::tr//*[contains(@class,'btn btn-primary')]")

            self._wait_for_visible(newly_added_element)
            self._click(newly_added_element)
            self.logger.info(f'{add_new_product} was successfully updated!')
            return self

    def set_meta_tag_of_product(self, meta_tag):
        with allure.step(f"заполняем параметр {meta_tag}"):
            self._wait_for_visible(AdminTool.general)
            self._click(AdminTool.general)
            self._input(AdminTool.meta_tag_title, meta_tag)
            return self

    def upload_new_image_avatar(self, image):
        with allure.step(f"загружаем новый аватар {image}"):
            self._wait_for_visible(AdminTool.image)
            self._click(AdminTool.image)
            self._wait_for_visible(AdminTool.default_image)
            self._click(AdminTool.default_image)
            self._wait_for_visible(AdminTool.image_manager)
            self._click(AdminTool.image_manager)
            self._wait_for_visible(AdminTool.image_upload)
            self.driver.execute_script("$('#button-upload').click();")

            file = self.driver.find_element(*AdminTool.file_upload)
            file.send_keys(image)
            ActionChains(self.driver).pause(1).perform()
            Alert(self.driver).accept()

        # file = self.driver.find_element(*AdminTool.file_upload)
        # file.send_keys(image)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.alert_is_present())
        # alert = self.driver.switch_to.alert
        # alert.accept()

        # self._wait_for_visible(AdminTool.image_upload)
        # self._wait_for_visible(AdminTool.new_avatar)
            self._click(AdminTool.new_avatar)
            self.logger.info(f'Avatar was successfully added!')
            return self

    def save_product(self):
        with allure.step(f"сохраняем продукт"):
            self._wait_for_visible(AdminTool.save_product)
            self._click(AdminTool.save_product)
            self.logger.info(f'Product was successfully saved!')
            return self
