import logging

if __name__ == "__main__":
    # the most basic logging setup
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Let's start the script")
    logging.warning("We'll this went not as planned")
    logging.debug("Very detailed info in process {}".format(__name__))
    logging.basicConfig(level=logging.INFO)
    logging.info("Level set to Info")
    logging.debug("Very detailed info in process {}".format(__name__))

    # which loggers are running?
    print(logging.Logger.manager.loggerDict)

    # get a customs loggers
    logger_project = logging.getLogger("projectlogger")
    logger_etl = logging.getLogger("projectlogger.etl")
    logger_modelling = logger_project.getChild("modeling")
    print(logging.Logger.manager.loggerDict)


    # stacktrace if needed
    logging.debug("hello", stack_info=True, exc_info=True)
