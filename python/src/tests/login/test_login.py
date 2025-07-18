# tests/test_login.py
import allure

# from src.pages.login_page import LoginPage
from pages.login_page import LoginPage
from core.config import Config


def test_login_success(page):
    login_page = LoginPage(page)
    login_page.login("luna.moon@maif.com", "123")
    login_page.expect_welcome_message()


@allure.title("Login with correct credentials using Allure annotations")
@allure.epic("Login")
@allure.feature("Authentication Flow")
@allure.story("User logs in with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "maicon.fang")
def test_login_success_allure(page):
    config = Config()
    login_page = LoginPage(page)

    with allure.step("Step 1: Navigate to login page"):
        login_page.navigate()

    with allure.step("Step 2: Submit login credentials"):
        login_page.login(config.get("username"), config.get("password"))

    with allure.step("Step 3: Validate successful login message"):
        login_page.expect_welcome_message()


def test_login_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.login("test001", "1234")
    login_page.expect_login_error()


def test_validation_short_inputs(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.fill_username("1")
    login_page.fill_password("1")
    page.get_by_text("Task Manager Plus The login").click()
    login_page.expect_short_login_error()
    login_page.expect_short_password_error()


def test_validation_max_length_inputs(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.fill_password("maxPassword maxPassword maxPassword maxPassword")
    login_page.fill_username("maxlogin maxlogin maxlogin maxlogin maxlogin maxlogin maxlogin")
    page.locator("section", has_text="Task Manager Plus The").locator("section").click()
    login_page.expect_max_login_length_error()
    login_page.expect_max_password_length_error()


def test_server_error_mock(page):
    def handle_route(route, request):
        route.fulfill(
            status=500,
            content_type="application/json",
            body='{"error":"Server not found"}'
        )

    page.route("**/oauth/token", handle_route)

    login_page = LoginPage(page)
    login_page.login("luna.moon@maif.com", "123")
    login_page.expect_server_not_found_error()



@allure.title("Intentional failure demo for Allure reporting")
@allure.epic("Demo")
@allure.feature("Failure Scenarios")
@allure.story("Test fails on purpose to show how Allure handles errors")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "maicon.fang")
def test_intentional_failure_demo(page):
    login_page = LoginPage(page)

    with allure.step("Step 1: Navigate to login page"):
        login_page.navigate()

    with allure.step("Step 2: Fail on purpose"):
        assert False, "❌ Intentional failure: this is for demo purposes only"

