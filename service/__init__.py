from pathlib import Path
import logging

PROJECT_ROOT = Path(__file__).parent.parent.resolve()

LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
logger = logging.basicConfig(format=LOG_FORMAT)
