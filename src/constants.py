from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Vector Database
VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"

# Config Directory
CONFIG_DIR = PROJECT_ROOT / "config"

# Logs
LOG_DIR = PROJECT_ROOT / "logs"

# Outputs
OUTPUT_DIR = PROJECT_ROOT / "outputs"