import logging
from logging import StreamHandler, Formatter
import logging_tree


if __name__ == "__main__":
    # printout shows the currently active loggers
    logging_tree.printout()
    # --> a root logger ist present, but not configured

    # # sent to root, but no result, because below warning
    logging.info("You can't see me")
    # # sent to root, with result, because "warning"
    logging.warning("This you can see!")

    # printout shows the currently active loggers
    logging_tree.printout()
    # --> now there is a handler and a formatter!

    # let's add some loggers
    logger_parent: logging.Logger = logging.getLogger("MyLogger")
    logger_child: logging.Logger = logging.getLogger("MyLogger.Sublogger")

    # testing the logger
    logger_parent.warning("Be warned, young padawan!")
    logger_child.error("Careful be, you must!")
    # -> both work without handler, because it's inherited from root
    logging_tree.printout()

    # add some handlers
    custom_console_output = StreamHandler()
    logger_parent.addHandler(custom_console_output)
    logger_parent.setLevel(logging.DEBUG)

    logger_parent.info("Luke, I'm your father")
    logger_child.info("Noooohhhh!")

    # The output is double, ... why?
    logging_tree.printout()
    # because it inherits from the root and the parent

    # let's disable the propagation
    logger_child.propagate = False
    logger_child.info("I only tell it once!")



    # ... not message, because no handler and no propagation
    print(logger_child.handlers)
    logger_child.addHandler(custom_console_output)
    logger_child.info("I only tell it once, for real!")
    # message, but no format.


    # adding a format
    formatter = Formatter('%(levelname)s - %(asctime)s – %(name)s - %(lineno)s - %(message)s')
    custom_console_output.formatter = formatter
    logger_child.info("I only tell it once, for real!")

