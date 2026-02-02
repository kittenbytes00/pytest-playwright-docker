import pytest
from playwright.sync_api import Page
from pages.sauce_login_page import SauceLoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_sauce_login_page_load(page: Page) -> None:
    login_page = SauceLoginPage(page)
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("load")
    page.wait_for_load_state("networkidle")

    login_page.launch_login_page()
    page.screenshot(path="screenshots/login/sauce_login.png")

@pytest.mark.regression
def test_sauce_successful_login(page: Page) -> None:
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
    page.screenshot(path="screenshots/login/sauce_login_successful.png")