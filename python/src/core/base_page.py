# src/core/base_page.py
from playwright.sync_api import Page
from .config import settings

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.timeout = settings.timeout

    def goto(self, path: str = "") -> None:
        """Navega combinando base URL + path."""
        url = f"{settings.base_url}{path}"
        self.page.goto(url, timeout=self.timeout)
