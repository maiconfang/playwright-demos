# pages/login_page.py
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:4200/#/login")

    def fill_username(self, username: str):
        self.page.get_by_role("textbox", name="Login").fill(username)

    def fill_password(self, password: str):
        self.page.get_by_role("textbox", name="Password").fill(password)

    def submit(self):
        self.page.get_by_role("button", name="Enter").click()

    def login(self, username: str, password: str):
        self.navigate()
        self.fill_username(username)
        self.fill_password(password)
        self.submit()

    def expect_welcome_message(self):
        expect(self.page.get_by_role("heading", name="Welcome to the System!")).to_be_visible()

    def expect_redirect_to_app(self):
        expect(self.page).to_have_url(r".*#\/app$")

    def expect_login_error(self):
        expect(self.page.get_by_role("alert", name="Invalid username or password")).to_be_visible()

    def expect_short_login_error(self):
        expect(
            self.page.locator("app-form-messages-error").filter(has_text="The login needs to have at")
        ).to_be_visible()

    def expect_short_password_error(self):
        expect(
            self.page.locator("app-form-messages-error").filter(has_text="The password needs to have at")
        ).to_be_visible()

    def expect_max_login_length_error(self):
        expect(
            self.page.get_by_text("The login may have at most")
        ).to_be_visible()

    def expect_max_password_length_error(self):
        expect(
            self.page.get_by_text("The password may have at most")
        ).to_be_visible()

    def expect_server_not_found_error(self):
        expect(self.page.get_by_text("Opps!! Error processing your request")).to_be_visible()
