# Task 2: Logging
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)

logging.debug("This is a debug message")
logging.info("The program started successfully!")
logging.warning("This is a warning message")
logging.error("An error occured")
logging.critical("The system has crashed")
