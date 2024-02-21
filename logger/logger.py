from logging import getLogger
import os

logger = getLogger(__name__)

def do_something():
    logger.info(f"Runnging {os.path.basename(__file__)}")