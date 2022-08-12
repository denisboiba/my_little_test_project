from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BTN = (By.CSS_SELECTOR, '[name = registration_submit]')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_COST = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
