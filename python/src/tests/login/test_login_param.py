import pytest
import allure
from pages.login_page import LoginPage

@allure.epic("Login")
@allure.feature("Authentication")
@allure.story("Login with multiple credentials")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("username,password", [
    ("luna.moon@maif.com", "123"),       # Valid user
    ("invalideeeeeeeeeeeee@user.com", "wrongpass"),   # Invalid user
])
def test_login_multiple_users(page, username, password):
    login_page = LoginPage(page)

    with allure.step(f"Navigate to login page"):
        login_page.navigate()

    with allure.step(f"Attempt login with {username}"):
        login_page.login(username, password)

    if username == "luna.moon@maif.com" and password == "123":
        with allure.step("Expect welcome message"):
            login_page.expect_welcome_message()
    else:
        with allure.step("Expect login error"):
            login_page.expect_login_error("Invalid username or password")
