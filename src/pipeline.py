"""
pipeline.py

Main ETL Pipeline
"""

import logging
from pathlib import Path
from src.utils.logger import logger
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

LOG_FOLDER = PROJECT_ROOT / "logs"
LOG_FOLDER.mkdir(exist_ok=True)

LOG_FILE = LOG_FOLDER / "pipeline.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def run(script):

    logging.info(f"Running {script}")

    result = subprocess.run(
        [sys.executable, script]
    )

    if result.returncode == 0:
        logging.info(f"{script} SUCCESS")
    else:
        logging.error(f"{script} FAILED")
        exit()


print("=" * 80)
print("N100 FINANCIAL INTELLIGENCE")
print("ETL PIPELINE")
print("=" * 80)

print("\nRunning Loader")
run("src/etl/loader.py")

print("\nRunning Validator")
run("src/etl/validator.py")

print("\n" + "=" * 80)
print("PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 80)

logging.info("Pipeline Finished Successfully")