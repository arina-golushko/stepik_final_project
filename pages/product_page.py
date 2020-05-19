from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def should_be_product_in_cart_message(self):
        assert self.is_text_in_element_present(*ProductPageLocators.PRODUCT_NAME) == \
        self.is_text_in_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_TO_CART_MESSAGE),\
        "Name of added product in confirmation message doesn't correspond to product's name"

    def should_be_price_message(self):
        assert self.is_text_in_element_present(*ProductPageLocators.PRODUCT_PRICE) == \
        self.is_text_in_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_CART_PRICE_MESSAGE),\
        "Price of added product doesn't correspond to product's price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_element_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element doesn't desappear"
