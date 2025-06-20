package com.maiconfang;

import com.microsoft.playwright.*;
import org.junit.jupiter.api.*;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class LoginPageTest {

    private Playwright playwright;
    private Browser browser;

    @BeforeAll
    void setUpAll() {
        playwright = Playwright.create();
        browser = playwright.chromium().launch(new BrowserType.LaunchOptions().setHeadless(false)); // true para rodar sem interface
    }

    @AfterAll
    void tearDownAll() {
        browser.close();
        playwright.close();
    }

    private Page page;
    private LoginPage loginPage;

    @BeforeEach
    void setUp() {
        BrowserContext context = browser.newContext(new Browser.NewContextOptions()
                .setBaseURL("http://localhost:4200"));
        page = context.newPage();
        loginPage = new LoginPage(page);
    }

    @AfterEach
    void tearDown() {
        page.context().close();
    }

    @Test
    void shouldLoginSuccessfullyAndRedirectToAppPage() {
        loginPage.login("luna.moon@maif.com", "123");
        loginPage.expectWelcomeMessage();
        loginPage.expectRedirectToApp();
    }

    @Test
    void shouldShowErrorWithInvalidCredentials() {
        loginPage.login("test001", "1234");
        loginPage.expectLoginError();
    }

    @Test
    void shouldShowValidationErrorsForShortLoginAndPassword() {
        loginPage.navigate();
        loginPage.fillUsername("1");
        loginPage.fillPassword("1");

        // Force validation by clicking away
        page.getByText("Task Manager Plus The login").click();

        loginPage.expectShortLoginError();
        loginPage.expectShortPasswordError();
    }

    @Test
    void shouldShowMaxLengthValidationErrorsForLoginAndPassword() {
        loginPage.navigate();

        loginPage.fillPassword("maxPassword maxPassword maxPassword maxPassword");
        loginPage.fillUsername("maxlogin maxlogin maxlogin maxlogin maxlogin maxlogin maxlogin");

        // Force validation by clicking away
        page.locator("section")
            .filter(new Locator.FilterOptions().setHasText("Task Manager Plus The"))
            .locator("section").click();

        loginPage.expectMaxLoginLengthError();
        loginPage.expectMaxPasswordLengthError();
    }

//    @Test
//    void shouldShowServerNotFoundErrorOnLoginWithMock() {
//        page.route("**/oauth/token", route -> {
//            route.fulfill(new Route.FulfillOptions()
//                .setStatus(500)
//                .setContentType("application/json")
//                .setBody("{\"error\": \"Server not found\"}")
//            );
//        });
//
//        loginPage.login("luna.moon@maif.com", "123");
//        loginPage.expectServerNotFoundError();
//    }
}
