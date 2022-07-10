import logging.config

logging_conf = \
    dict(version=1,
         formatters=dict(
             defaultFormatter={'format': '%(levelname)s - %(asctime)s - %(name)s - %(lineno)s - %(message)s'}),
         handlers=dict(consoleHandler={'class': 'logging.StreamHandler',
                                       'level': logging.INFO,
                                       'formatter': 'defaultFormatter'},
                       writeFileHandler={'class': 'logging.FileHandler', 'level': logging.DEBUG,
                                         'formatter': 'defaultFormatter',
                                         'filename': 'test_hello.log',
                                         'mode': 'a'}),
         loggers=dict(logger2file=dict(handlers=['writeFileHandler'],
                                       qualname='btelligentLogger',
                                       level=logging.DEBUG)),
         root=dict(level=logging.INFO,
                   handlers=['consoleHandler'])

         )

if __name__ == "__main__":
    logging.config.dictConfig(logging_conf)

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
