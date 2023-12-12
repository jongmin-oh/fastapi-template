import time
from app.utility.logger import console_logger


def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start = time.time()
        result = original_fn(*args, **kwargs)
        fn_time = round((time.time() - start), 5)
        log_message = f"{original_fn.__name__} time : {fn_time}"
        console_logger.info(log_message)
        return result

    return wrapper_fn


def async_logging_time(original_fn):
    async def wrapper_fn(*args, **kwargs):
        start = time.time()
        result = await original_fn(*args, **kwargs)
        fn_time = round((time.time() - start), 5)
        log_message = f"{original_fn.__name__} time : {fn_time}"
        console_logger.info(log_message)
        return result

    return wrapper_fn
