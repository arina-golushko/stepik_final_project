from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_products_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
        "There is nothing in basket"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
        "There are some products in basket"

    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        "Basket isn't empty"

    def should_not_be_basket_is_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        "Basket isn't empty"