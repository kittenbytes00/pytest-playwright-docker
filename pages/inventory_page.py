from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.swag_labs_label = page.locator("//div[contains(text(), 'Swag Labs')]")
        self.products_label = page.locator("//span[contains(text(), 'Products')]")
        self.product_sort_container = page.locator("//select[@class='product_sort_container']")
        self.add_to_cart_sauce_labs_backpack = page.locator(
            "//button[@id='add-to-cart-sauce-labs-backpack']"
        )
        self.shopping_cart_container = page.locator("//div[@id='shopping_cart_container']")

    def is_swag_labs_label_visible(self):
        expect(self.swag_labs_label).to_be_visible(timeout=10000)

    def is_products_label_visible(self):
        expect(self.products_label).to_be_visible(timeout=10000)

    def is_product_sort_container_visible(self):
        expect(self.product_sort_container).to_be_visible(timeout=10000)

    def is_shopping_cart_container_visible(self):
        expect(self.shopping_cart_container).to_be_visible(timeout=10000)

    def is_add_to_cart_sauce_labs_backpack_visible(self):
        expect(self.add_to_cart_sauce_labs_backpack).to_be_visible(timeout=10000)

    def validate_inventory_page_load(self):
        expect(self.swag_labs_label).to_be_visible(timeout=10000)
        expect(self.products_label).to_be_visible(timeout=10000)
        expect(self.product_sort_container).to_be_visible(timeout=10000)
        expect(self.add_to_cart_sauce_labs_backpack).to_be_visible(timeout=10000)
        expect(self.shopping_cart_container).to_be_visible(timeout=10000)

    def add_to_cart(self):
        self.add_to_cart_sauce_labs_backpack.click()

    def click_cart(self):
        self.shopping_cart_container.click()
