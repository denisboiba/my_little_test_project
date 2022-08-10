from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Product is presented in the basket, but should not be"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Empty message isn't presented"
