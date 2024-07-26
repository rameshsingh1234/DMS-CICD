import logging
import os

def setup_logger(logger_name, log_file, level=logging.WARNING):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Erase log if already exists
    if os.path.exists(log_file):
        os.remove(log_file)

    # Configure log file
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s')
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
