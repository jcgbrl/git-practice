import logging

def test_Logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("a debug statement is executed")
    logger.info("information statement")
    logger.debug("a debug statement is executed")
    logger.warning("something is in warning mode")
    logger.error("an error has happened")
    logger.critical("something is in critical mode")
