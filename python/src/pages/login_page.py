# src/pages/login_page.py

from playwright.sync_api import Page, expect
from src.core.base_page import BasePage
from src.core.config import settings


class LoginPage(BasePage):
    _username_field = ("textbox", "Login")
    _password_field = ("textbox", "Password")
    _enter_button = ("button", "Enter")

    def navigate(self) -> None:
        """Navigate directly to the login route using BasePage's goto."""
        self.goto(settings.login_path)

    def fill_username(self, username: str) -> None:
        role, name = self._username_field
        self.page.get_by_role(role, name=name).fill(username)

    def fill_password(self, password: str) -> None:
        role, name = self._password_field
        self.page.get_by_role(role, name=name).fill(password)

    def submit(self) -> None:
        role, name = self._enter_button
        self.page.get_by_role(role, name=name).click()

    def login(self, username: str, password: str) -> None:
        self.navigate()
        self.fill_username(username)
        self.fill_password(password)
        self.submit()

    def expect_welcome_message(self) -> None:
        expect(self.page.get_by_role("heading", name="Welcome to the System!")).to_be_visible()

    def expect_redirect_to_app(self) -> None:
        expect(self.page).to_have_url(r".*#\/app$")

    def expect_login_error(self) -> None:
        expect(self.page.get_by_role("alert", name="Invalid username or password")).to_be_visible()

    def expect_short_login_error(self) -> None:
        expect(
            self.page.locator("app-form-messages-error").filter(
                has_text="The login needs to have at"
            )
        ).to_be_visible()

    def expect_short_password_error(self) -> None:
        expect(
            self.page.locator("app-form-messages-error").filter(
                has_text="The password needs to have at"
            )
        ).to_be_visible()

    def expect_max_login_length_error(self) -> None:
        expect(
            self.page.get_by_text("The login may have at most")
        ).to_be_visible()

    def expect_max_password_length_error(self) -> None:
        expect(
            self.page.get_by_text("The password may have at most")
        ).to_be_visible()

    def expect_server_not_found_error(self) -> None:
        expect(self.page.get_by_text("Opps!! Error processing your request")).to_be_visible()
