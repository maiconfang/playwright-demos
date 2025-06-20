const { test } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');

test('should login successfully and redirect to app page', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.login('luna.moon@maif.com', '123');
  await loginPage.expectWelcomeMessage();
  await loginPage.expectRedirectToApp();
});

test('should show error with invalid credentials', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.login('test001', '1234');
  await loginPage.expectLoginError();
});

test('should show validation errors for short login and password', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.navigate(); // Open /#/login
  await loginPage.fillUsername('1'); // Login invalid
  await loginPage.fillPassword('1'); // Password invalid

  // Click outside to force validation
  await page.getByText('Task Manager Plus The login').click();

  // Check specific error messages
  await loginPage.expectShortLoginError();
  await loginPage.expectShortPasswordError();
});

test('should show max length validation errors for login and password', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.navigate();
  await loginPage.fillPassword('maxPassword maxPassword maxPassword maxPassword');
  await loginPage.fillUsername('maxlogin maxlogin maxlogin maxlogin maxlogin maxlogin maxlogin');

  // Click outside to trigger validation
  await page.locator('section').filter({ hasText: 'Task Manager Plus The' }).locator('section').click();

  // Validates maximum length errors
  await loginPage.expectMaxLoginLengthError();
  await loginPage.expectMaxPasswordLengthError();
});

test('should show server not found error on login (with mock)', async ({ page }) => {
  await page.route('**/oauth/token', route => {
    route.fulfill({
      status: 500,
      contentType: 'application/json',
      body: JSON.stringify({ error: 'Server not found' }),
    });
  });

  const loginPage = new LoginPage(page);
  await loginPage.login('luna.moon@maif.com', '123');
  await loginPage.expectServerNotFoundError();
});
