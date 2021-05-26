import logging
import os
from src.config import Config


class Logger:

    """
    Used for logging
    """

    def __init__(self, log_type):
        """
        Constructor function
        :param log_type: type of log(database or webcrawler vs.)
        :type log_type: str
        :return: none
        """
        self.log_type = log_type
        self.log_file = Config.LOG_FILE
        self.log_format = Config.LOG_FORMAT
        self.close_log()
        self.logger = self.get_log_config()

    def log(self, level, msg):
        """
        Log info/warning/error message in log file.
        :param level: message level
        :type level: str
        :param msg: message
        :type msg: str
        :return: none
        """
        if self.logger is not None:
            if level == logging.INFO:
                self.logger.info("{}".format(msg))
            elif level == logging.WARNING:
                self.logger.warning("{}".format(msg))
            else:
                self.logger.error("{}".format(msg))

    def get_log_config(self):
        """
        Configuration for logging
        :param: none
        :return: none
        """
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # create logger
        logger = logging.getLogger(self.log_type)
        # create handler
        file_path = os.path.abspath(self.log_file)
        handler = logging.FileHandler(file_path)
        # create formatter
        formatter = logging.Formatter(self.log_format)
        # set Formatter
        handler.setFormatter(formatter)
        # add handler
        logger.addHandler(handler)
        # set level
        logger.setLevel(logging.INFO)

        return logger
    

    def close_log(self):
        """
        Remove all logger
        :param: none
        :return: none
        """
        logger = logging.getLogger(self.log_type)
        while logger.hasHandlers():
            logger.removeHandler(logger.handlers[0])
