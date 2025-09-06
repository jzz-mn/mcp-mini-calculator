import json
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.json"

HOST = "127.0.0.1"
PORT = 8000

def load_config() -> dict:
    """Load optional static config from JSON file."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}  # default empty config

# Example usage:
# config = load_config()
# print(config.get("greeting_prefix", "Hello"))
