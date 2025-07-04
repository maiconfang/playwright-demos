using System.Text.RegularExpressions;
using Microsoft.Playwright;
// using Microsoft.Playwright.Assertions;
// using static Microsoft.Playwright.Assertions;

namespace Pages;

public class LoginPage
{
    private readonly IPage _page;

    // ────────── Locators (semelhantes às tuplas do Python) ──────────
    private (AriaRole role, string name) _usernameField = (AriaRole.Textbox, "Login");
    private (AriaRole role, string name) _passwordField = (AriaRole.Textbox, "Password");
    private (AriaRole role, string name) _enterButton   = (AriaRole.Button,  "Enter");

    public LoginPage(IPage page)
    {
        _page = page;
    }

    // ────────── Ações ──────────
    public async Task NavigateAsync()
    {
        await _page.GotoAsync("/#/login");

        // Waits until the login field is visible
        await _page.Locator("#login_username").WaitForAsync(new() {
            State = WaitForSelectorState.Visible,
            Timeout = 5000 // 5 segundos
        });
    }
    

    public async Task FillUsernameAsync(string username)
    {
        var (role, name) = _usernameField;
        await _page.GetByRole(role, new() { Name = name }).FillAsync(username);
    }

    public async Task FillPasswordAsync(string password)
    {
        var (role, name) = _passwordField;
        await _page.GetByRole(role, new() { Name = name }).FillAsync(password);
    }

    public async Task SubmitAsync()
    {
        var (role, name) = _enterButton;
        await _page.GetByRole(role, new() { Name = name }).ClickAsync();
    }

    public async Task LoginAsync(string username, string password)
    {
        await NavigateAsync();
        await FillUsernameAsync(username);
        await FillPasswordAsync(password);
        await SubmitAsync();
    }

    // ────────── Expectations ──────────
    public async Task ExpectWelcomeMessageAsync()
    {
        await Assertions.Expect(
            _page.GetByRole(AriaRole.Heading, new() { Name = "Welcome to the System!" })
        ).ToBeVisibleAsync();
    }

    public async Task ExpectRedirectToAppAsync()
    {
        await Assertions.Expect(_page).ToHaveURLAsync(new Regex(@".*#\/app$"));
    }

    public async Task ExpectLoginErrorAsync()
    {
        await Assertions.Expect(
            _page.GetByRole(AriaRole.Alert, new() { Name = "Invalid username or password" })
        ).ToBeVisibleAsync();
    }

    public async Task ExpectShortLoginErrorAsync()
    {
        await Assertions.Expect(
            _page.Locator("app-form-messages-error")
                 .Filter(new() { HasTextString = "The login needs to have at" })
        ).ToBeVisibleAsync();
    }

    public async Task ExpectShortPasswordErrorAsync()
    {
        await Assertions.Expect(
            _page.Locator("app-form-messages-error")
                 .Filter(new() { HasTextString = "The password needs to have at" })
        ).ToBeVisibleAsync();
    }

    public async Task ExpectMaxLoginLengthErrorAsync()
    {
        await Assertions.Expect(
            _page.GetByText("The login may have at most")
        ).ToBeVisibleAsync();
    }

    public async Task ExpectMaxPasswordLengthErrorAsync()
    {
        await Assertions.Expect(
            _page.GetByText("The password may have at most")
        ).ToBeVisibleAsync();
    }

    public async Task ExpectServerNotFoundErrorAsync()
    {
        await Assertions.Expect(
            _page.GetByText("Opps!! Error processing your request")
        ).ToBeVisibleAsync();
    }
}
