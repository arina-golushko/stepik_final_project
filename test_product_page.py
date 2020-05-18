import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    alert_window = BasePage(browser, link)
    alert_window.solve_quiz_and_get_code()
    page.should_be_product_in_cart_message()
    page.should_be_price_message()

@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
                                  "?promo=offer4", "?promo=offer5", "?promo=offer6",
                                  pytest.param("?promo=offer7", marks = pytest.mark.xfail 
                                  (reason = "Added to cart product name doesn't correspond to catalogue product name")),
                                  "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket_on_promo_pages(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    browser.get(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    alert_window = BasePage(browser, link)
    alert_window.solve_quiz_and_get_code()
    page.should_be_product_in_cart_message()

