# src/core/config.py
from dataclasses import dataclass
import os

@dataclass
class Settings:
    base_url: str = os.getenv("BASE_URL", "http://localhost:4200/#")
    login_path: str = "/login"
    timeout: int = 10_000  # ms

settings = Settings()  # ✅ ESSA LINHA DEVE EXISTIR
