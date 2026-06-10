import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# UI (SauceDemo)
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
CHROME_BIN = os.getenv("CHROME_BIN", "")
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "")

# API
JSONPLACEHOLDER_BASE_URL = os.getenv(
    "JSONPLACEHOLDER_BASE_URL", "https://jsonplaceholder.typicode.com"
)

# Credentials (SauceDemo demo accounts)
STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
STANDARD_PASSWORD = os.getenv("STANDARD_PASSWORD", "secret_sauce")
LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")

SCREENSHOTS_DIR = BASE_DIR / "screenshots"
