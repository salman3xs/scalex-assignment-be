import os
from pathlib import Path


# --- JWT Configuration ---
JWT_SECRET_KEY = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
JWT_ALGORITHM = "HS256"
JWT_EXPIRY_MINUTES = 1440  # 24 hours

# --- Server Configuration ---
HOST = "0.0.0.0"
PORT = 8000

# --- File Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
REGULAR_CSV_PATH = DATA_DIR / "regularUser.csv"
ADMIN_CSV_PATH = DATA_DIR / "adminUser.csv"
