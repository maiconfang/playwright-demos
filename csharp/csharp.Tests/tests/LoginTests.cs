using Microsoft.Playwright.NUnit;
using NUnit.Framework;
using Pages;
using Core;
using System.Text.RegularExpressions;
using Microsoft.Playwright;

namespace Tests;

// [Parallelizable(ParallelScope.All)]
[NonParallelizable]
[TestFixture]
public class LoginTests : PageTest
{
    // ── Browser context (baseURL, viewport etc.) ──
    public override BrowserNewContextOptions ContextOptions() => new()
    {
        BaseURL      = TestConfig.BaseUrl,
        ViewportSize = new() { Width = 1280, Height = 720 }
    };

    // ───────────────────── Test cases ─────────────────────
    [Test]
    public async Task LoginSuccess()
    {
        var loginPage = new LoginPage(Page);

        await loginPage.LoginAsync("luna.moon@maif.com", "123");
        await loginPage.ExpectWelcomeMessageAsync();
    }

    [Test]
    public async Task LoginInvalidCredentials()
    {
        var loginPage = new LoginPage(Page);

        await loginPage.LoginAsync("test001", "1234");
        await loginPage.ExpectLoginErrorAsync();
    }

    [Test]
    public async Task ValidationShortInputs()
    {
        var loginPage = new LoginPage(Page);

        await loginPage.NavigateAsync();
        await loginPage.FillUsernameAsync("1");
        await loginPage.FillPasswordAsync("1");

        // Click outside to trigger validation
        await Page.GetByText("Task Manager Plus The login").ClickAsync();

        await loginPage.ExpectShortLoginErrorAsync();
        await loginPage.ExpectShortPasswordErrorAsync();
    }

    [Test]
    public async Task ValidationMaxLengthInputs()
    {
        var loginPage = new LoginPage(Page);

        await loginPage.NavigateAsync();
        await loginPage.FillPasswordAsync("maxPassword maxPassword maxPassword maxPassword");
        await loginPage.FillUsernameAsync("maxlogin maxlogin maxlogin maxlogin maxlogin maxlogin maxlogin");

        await Page.Locator("section", new() { HasTextString = "Task Manager Plus The" })
                  .Locator("section")
                  .ClickAsync();

        await loginPage.ExpectMaxLoginLengthErrorAsync();
        await loginPage.ExpectMaxPasswordLengthErrorAsync();
    }

    [Test]
    public async Task ServerErrorMock()
    {
        // Intercepts the request and returns a 500 error
        await Page.RouteAsync("**/oauth/token", async route =>
        {
            await route.FulfillAsync(new RouteFulfillOptions
            {
                Status      = 500,
                ContentType = "application/json",
                Body        = "{\"error\":\"Server not found\"}"
            });
        });

        var loginPage = new LoginPage(Page);
        await loginPage.LoginAsync("luna.moon@maif.com", "123");
        await loginPage.ExpectServerNotFoundErrorAsync();
    }
}
