import pytest
from selenium import webdriver
from .pages.product_page import ProductPage


@pytest.mark.parametrize('num',
                         [*range(7),
                          pytest.param('7', marks=pytest.mark.xfail(reason='bugged page')),
                          *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_presented_items()
    page.should_be_equals_items()
