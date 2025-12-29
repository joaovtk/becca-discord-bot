import logging

FORMAT = "%(asctime)s %(message)s"

logging.basicConfig(format=FORMAT, level=logging.INFO, filename="main.log")
logger = logging.getLogger(__name__).setLevel(logging.ERROR)

