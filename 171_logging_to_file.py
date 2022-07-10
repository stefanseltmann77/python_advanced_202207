import logging

if __name__ == "__main__":
    # logging to file
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s - %(asctime)s - %(name)s - %(lineno)s - %(message)s',
                        filename="hello.log", filemode='a')

    # call root logger
    logger = logging.getLogger()
    logger.info("Let's start the script")
    logger.warning("We'll this went not as planned")
    logger.debug("Very detailed info in process {}".format(__name__))
    logger.setLevel(logging.INFO)
    logger.info("Level set to Info")
    logger.debug("Very detailed info in process {}".format(__name__))

