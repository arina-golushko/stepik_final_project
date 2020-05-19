from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_NAME_IN_ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    PRODUCT_PRICE_IN_CART_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini .btn")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
