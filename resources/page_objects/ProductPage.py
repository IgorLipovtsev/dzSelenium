from resources.locators import Product
from resources.page_objects.common import BasePage

class ProductPage(BasePage):

    def add_to_wishlist(self):
        self._click(Product.add_to_wishlist)

    def add_to_cart(self):
        self._click(Product.add_to_cart)
