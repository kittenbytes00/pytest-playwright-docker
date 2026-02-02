import pytest
from playwright.sync_api import Page
from pages.sauce_login_page import SauceLoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.regression
@pytest.mark.smoke
def test_purchase_successful(page: Page) -> None:
    login_page = SauceLoginPage(page)
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("load")
    page.wait_for_load_state("networkidle")

    login_page.launch_login_page()
    login_page.login_to_sauce_app(username_input="standard_user", password_input="secret_sauce")
    page.wait_for_load_state("load")
    page.wait_for_load_state("networkidle")

    inventory_page = InventoryPage(page)
    inventory_page.validate_inventory_page_load()
    inventory_page.add_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(page)
    cart_page.is_your_cart_label_visible()
    cart_page.is_cart_contents_container_visible()
    cart_page.is_checkout_visible()
    page.screenshot(path="screenshots/purchase/add_to_cart_successful.png")

    cart_page.click_checkout()
    page.screenshot(path="screenshots/checkout_your_info/checkout_your_info_load.png")