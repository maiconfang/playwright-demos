# tests/test_login.py

# from src.pages.login_page import LoginPage
from pages.login_page import LoginPage


def test_login_success(page):
    login_page = LoginPage(page)
    login_page.login("luna.moon@maif.com", "123")
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


def test_intentional_failure_demo(page):
    login_page = LoginPage(page)
    login_page.navigate()
    # This test will fail on purpose to demonstrate test reports
    assert False, "Intentional failure: this is for demo purposes only"
