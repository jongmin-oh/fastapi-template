import logging


class Loggers:
    def get_console_logger(self):
        logger = logging.getLogger("Stream")

        if len(logger.handlers) > 0:
            return logger

        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("[%(levelname)s] %(asctime)s > %(message)s")

        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.DEBUG)
        streamHandler.setFormatter(formatter)

        logger.addHandler(streamHandler)
        return logger

    def get_file_logger(self):
        logger = logging.getLogger("File")

        if len(logger.handlers) > 0:
            return logger

        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(message)s")

        file_handler = logging.FileHandler("logs/data.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger


console_logger = Loggers().get_console_logger()
file_logger = Loggers().get_file_logger()
