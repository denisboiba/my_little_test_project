from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_presented_items(self):
        self.should_be_product_in_the_basket()
        self.should_be_basket_cost()

    def should_be_equals_items(self):
        self.should_names_equals()
        self.should_costs_equals()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button isn't presented"

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_product_in_the_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_THE_BASKET), "Product isn't presented"

    def should_names_equals(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_in_the_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_THE_BASKET)
        assert product_in_the_basket.text == product_name.text, "Product in the basket doesn't equals our product"

    def should_be_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST), "Basket cost isn't presented"

    def should_costs_equals(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
        assert basket_cost.text == product_price.text, "Basket cost doesn't equals product price"
