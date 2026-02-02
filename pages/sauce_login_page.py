from playwright.sync_api import Page, expect


class SauceLoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("//*[@id='user-name']")
        self.password = page.locator("//*[@id='password']")
        self.login = page.locator("//*[@id='login-button']")

    def is_username_visible(self):
        expect(self.username).to_be_visible(timeout=10000)

    def is_password_visible(self):
        expect(self.password).to_be_visible(timeout=10000)

    def is_login_visible(self):
        expect(self.login).to_be_visible(timeout=10000)

    def launch_login_page(self):
        expect(self.username).to_be_visible(timeout=10000)
        expect(self.password).to_be_visible(timeout=10000)
        expect(self.login).to_be_visible(timeout=10000)

    def enter_username(self, username_input: str):
        self.username.fill(username_input)

    def enter_password(self, password_input: str):
        self.password.fill(password_input)

    def click_login(self):
        self.login.click()

    def login_to_sauce_app(self, username_input: str, password_input: str):
        self.username.fill(username_input)
        self.password.fill(password_input)
        self.login.click()
