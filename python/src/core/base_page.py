# src/core/base_page.py
from playwright.sync_api import Page
from .config import Config


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.timeout = 5000  # or use a fixed value for now
        self.base_url = Config().get("base_url")

    def goto(self, path: str = "") -> None:
        """Navigate to a specific path combined with the base URL."""
        url = f"{self.base_url}{path}"
        self.page.goto(url, timeout=self.timeout)
