from playwright.sync_api import Page, expect

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.your_cart_label = page.locator("//span[contains(text(), 'Your Cart')]")
        self.cart_contents_container = page.locator("//div[@id='cart_contents_container']")
        self.checkout = page.locator("//button[@id='checkout']")

    def is_your_cart_label_visible(self):
        expect(self.your_cart_label).to_be_visible(timeout=10000)

    def is_cart_contents_container_visible(self):
        expect(self.cart_contents_container).to_be_visible(timeout=10000)

    def is_checkout_visible(self):
        expect(self.checkout).to_be_visible(timeout=10000)

    def validate_cart_page_load(self):
        expect(self.your_cart_label).to_be_visible(timeout=10000)

    def click_checkout(self):
        self.checkout.click()