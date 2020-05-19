from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no Login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no registration form"

    def register_new_user(self, email, password, confirm_password):
        email_address = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_ADDRESS).send_keys(email)
        self.email_address = email
        password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.password = password
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).send_keys(confirm_password)
        self.confirm_password = confirm_password
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
