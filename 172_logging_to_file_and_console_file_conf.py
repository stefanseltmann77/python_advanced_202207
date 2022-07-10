import logging
import logging.config

if __name__ == "__main__":
    logging.config.fileConfig("172_logging_to_file_and_console.ini")

    # call root logger
    logger = logging.getLogger("btelligentLogger")
    logger.info("Let's start the script")
    logger.warning("We'll this went not as planned")
    logger.debug(f"Very detailed fist info in process {__name__}")
    logger.setLevel(logging.INFO)
    logger.info("Level set to Info")
    logger.debug(f"Very detailed second info in process {__name__}")
    logging.getLogger("btelligentLogger").setLevel(logging.DEBUG)
    logger.debug(f"Very detailed third info in process {__name__}")

