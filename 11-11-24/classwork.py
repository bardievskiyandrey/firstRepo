import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", encoding="UTF-8", format="We have next log message: %(levelname)s:%(asctime)s - &(message)s")
logging.debug("Debug message ававав")
logging.info("Info message")
logging.warning("warning message")
logging.error("error message ")
logging.critical("critical message ")
