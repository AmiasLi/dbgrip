import logging
from types import FrameType
from typing import cast

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        cframe, depth = logging.currentframe(), 2
        while cframe.f_code.co_filename == logging.__file__:
            cframe = cast(FrameType, cframe.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )
