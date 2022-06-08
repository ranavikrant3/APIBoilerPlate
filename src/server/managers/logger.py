
from src.server.config.config import Logger
import logging
import logging.config
import os
from datetime import datetime


__logger = None

def init_app(app):
    """
    Initialize the application for the use with the logger setup.

    :param app: Application server

    :return __logger: Logger context
    """

    # Get the log path and create the directory if not exist
    Logger["handlers"]['file']['filename'] = eval(Logger.get("handlers").get('file').get("filename"))

    file_path = Logger.get("handlers").get('file').get("filename")
    log_path = os.path.dirname(file_path)
    if not os.path.exists(log_path):
       os.makedirs(log_path)

    # Configure the logger with the config standalone.json.run file
    logging.config.dictConfig(Logger)

    # Make a global variable for the logger
    global __logger
    __logger = logging.getLogger(app.config['API_NAME'])



def error(msg, *args, **kwargs):
    """Represents an internal error. Execution is unrecoverable."""
    __logger.error(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    """Represents an application error."""
    __logger.exception(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    """Verbose messages with debugging information."""
    __logger.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """Represents informational messages."""
    __logger.info(msg, *args, **kwargs)
