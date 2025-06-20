package com.maiconfang;

import com.microsoft.playwright.Page;
import com.microsoft.playwright.Locator;
import com.microsoft.playwright.assertions.PlaywrightAssertions;
import com.microsoft.playwright.options.AriaRole;

import java.util.regex.Pattern;

public class LoginPage {
    private final Page page;

    public LoginPage(Page page) {
        this.page = page;
    }

    public void navigate() {
        page.navigate("/#/login");
    }

    public void fillUsername(String username) {
        page.getByRole(AriaRole.TEXTBOX, new Page.GetByRoleOptions().setName("Login"))
            .fill(username);
    }

    public void fillPassword(String password) {
        page.getByRole(AriaRole.TEXTBOX, new Page.GetByRoleOptions().setName("Password"))
            .fill(password);
    }

    public void submit() {
        page.getByRole(AriaRole.BUTTON, new Page.GetByRoleOptions().setName("Enter"))
            .click();
    }

    public void login(String username, String password) {
        navigate();
        fillUsername(username);
        fillPassword(password);
        submit();
    }

    public void expectWelcomeMessage() {
        PlaywrightAssertions.assertThat(
            page.getByRole(AriaRole.HEADING, new Page.GetByRoleOptions().setName("Welcome to the System!"))
        ).isVisible();
    }

    public void expectRedirectToApp() {
        PlaywrightAssertions.assertThat(page)
            .hasURL(Pattern.compile("#/app$"));
    }

    public void expectLoginError() {
        PlaywrightAssertions.assertThat(
            page.getByRole(AriaRole.ALERT, new Page.GetByRoleOptions().setName("Invalid username or password"))
        ).isVisible();
    }

    public void expectShortLoginError() {
        PlaywrightAssertions.assertThat(
            page.locator("app-form-messages-error")
                .filter(new Locator.FilterOptions().setHasText("The login needs to have at"))
        ).isVisible();
    }

    public void expectShortPasswordError() {
        PlaywrightAssertions.assertThat(
            page.locator("app-form-messages-error")
                .filter(new Locator.FilterOptions().setHasText("The password needs to have at"))
        ).isVisible();
    }

    public void expectMaxLoginLengthError() {
        PlaywrightAssertions.assertThat(
            page.getByText(Pattern.compile("The login may have at most"))
        ).isVisible();
    }

    public void expectMaxPasswordLengthError() {
        PlaywrightAssertions.assertThat(
            page.getByText(Pattern.compile("The password may have at most"))
        ).isVisible();
    }

    public void expectServerNotFoundError() {
        PlaywrightAssertions.assertThat(
            page.getByText("Opps!! Error processing your request")
        ).isVisible();
    }
}
