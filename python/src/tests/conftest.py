import pytest
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Yield to get the actual test result object
    outcome = yield
    rep = outcome.get_result()

    # Only proceed if the test phase is "call" and the test has failed
    if rep.when == "call" and rep.failed:
        # Try to get the Playwright page fixture from the test context
        page = item.funcargs.get("page", None)
        if page:
            # Capture a screenshot of the current page state
            screenshot = page.screenshot()
            # Attach the screenshot to the Allure report
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
