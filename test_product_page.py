import time
import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.need_review
@pytest.mark.registered
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
    	link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    	page = LoginPage(browser, link)
    	page.open()
    	page.register_new_user(email = str(time.time()) + "@fakemail.org", password="stepiktest", confirm_password="stepiktest")
    	page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_product_in_cart_message()   


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    alert_window = BasePage(browser, link)
    alert_window.solve_quiz_and_get_code()
    page.should_be_product_in_cart_message()
    page.should_be_price_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty_message()
    basket_page.should_not_be_products_in_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
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

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
