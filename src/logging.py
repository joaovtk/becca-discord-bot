import logging

FORMAT = "%(asctime)s %(message)s"

logging.basicConfig(format=FORMAT, level=logging.WARNING)
logger = logging.getLogger(__name__)

logger.debug("Started Log")
