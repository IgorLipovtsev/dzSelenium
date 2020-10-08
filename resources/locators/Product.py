from selenium.webdriver.common.by import By


class Product:
    add_to_wishlist = (By.CSS_SELECTOR, '.btn-group [data-original-title="Add to Wish List"]')
    add_to_cart = (By.CSS_SELECTOR, '#button-cart')
