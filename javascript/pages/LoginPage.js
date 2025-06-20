const { expect } = require('@playwright/test');

class LoginPage {
  constructor(page) {
    this.page = page;
  }

  async navigate() {
    await this.page.goto('/#/login');
  }

  async fillUsername(username) {
    await this.page.getByRole('textbox', { name: 'Login' }).fill(username);
  }

  async fillPassword(password) {
    await this.page.getByRole('textbox', { name: 'Password' }).fill(password);
  }

  async submit() {
    await this.page.getByRole('button', { name: 'Enter' }).click();
  }

  async login(username, password) {
    await this.navigate();
    await this.fillUsername(username);
    await this.fillPassword(password);
    await this.submit();
  }

  async expectWelcomeMessage() {
    await expect(this.page.getByRole('heading', { name: 'Welcome to the System!' })).toBeVisible();
  }

  async expectRedirectToApp() {
    await expect(this.page).toHaveURL(/#\/app$/);
  }

  async expectLoginError() {
    await expect(this.page.getByRole('alert', { name: 'Invalid username or password' })).toBeVisible();
  }

  async expectShortLoginError() {
    await expect(
      this.page.locator('app-form-messages-error').filter({ hasText: 'The login needs to have at' })
    ).toBeVisible();
  }

  async expectShortPasswordError() {
    await expect(
      this.page.locator('app-form-messages-error').filter({ hasText: 'The password needs to have at' })
    ).toBeVisible();
  }

  async expectMaxLoginLengthError() {
    await expect(
      this.page.getByText(/The login may have at most/)
    ).toBeVisible();
  }

  async expectMaxPasswordLengthError() {
    await expect(
      this.page.getByText(/The password may have at most/)
    ).toBeVisible();
  }

  async expectServerNotFoundError() {
    await expect(this.page.getByText('Opps!! Error processing your request')).toBeVisible();
  }
}

module.exports = { LoginPage };
