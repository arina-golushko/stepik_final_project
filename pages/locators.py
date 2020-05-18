from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_NAME_IN_ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    PRODUCT_PRICE_IN_CART_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(3) strong")
