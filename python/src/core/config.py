import os
import json
from pathlib import Path

class Config:
    def __init__(self):
        env = os.getenv("ENV", "local")  # Defaults to local
        config_path = Path(__file__).parent.parent.parent / f"configs/config_{env}.json"

        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")

        with open(config_path, encoding="utf-8") as f:
            self.data = json.load(f)

    def get(self, key: str):
        return self.data.get(key)
