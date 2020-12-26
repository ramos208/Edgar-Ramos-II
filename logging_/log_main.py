import logging
import coloredlogs

coloredlogs.install()
logging.warning("a warning")
logging.error("some error")
logging.info("some info")