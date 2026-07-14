"""
pipeline.py

Main ETL Pipeline
"""

import subprocess
import sys
from pathlib import Path

from src.utils.logger import logger

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run(script):

    logger.info(f"Running {script}")

    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / script)]
    )

    if result.returncode == 0:
        logger.info(f"{script} SUCCESS")
    else:
        logger.error(f"{script} FAILED")
        sys.exit()


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

logger.info("Pipeline Finished Successfully")