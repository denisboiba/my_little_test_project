from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert login_url, "login_url  is not in current_url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        field1 = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        field1.send_keys(email)

        field2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        field2.send_keys(password)

        field3 = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD)
        field3.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        button.click()
