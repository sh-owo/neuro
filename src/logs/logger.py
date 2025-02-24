import logging
import os
from datetime import datetime
from typing import Optional, Dict

class AsyncLoggerSetup:
    _instances: Dict[str, logging.Logger] = {}

    @classmethod
    async def setup_logger(
        cls,
        name: str = __name__,
        level: int = logging.INFO,
        log_file: Optional[str] = None
    ) -> logging.Logger:
        if name not in cls._instances:
            logger = logging.getLogger(name)
            logger.setLevel(level)

            if not logger.handlers:
                formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                )

                stream_handler = logging.StreamHandler()
                stream_handler.setFormatter(formatter)
                logger.addHandler(stream_handler)

                if log_file:
                    os.makedirs('logs', exist_ok=True)
                    file_handler = logging.FileHandler(
                        f'logs/{log_file}_{datetime.now().strftime("%Y%m%d")}.log'
                    )
                    file_handler.setFormatter(formatter)
                    logger.addHandler(file_handler)

            cls._instances[name] = logger

        return cls._instances[name]

async def setup_logger(
    name: str = __name__,
    level: int = logging.INFO,
    log_file: Optional[str] = None
) -> logging.Logger:
    return await AsyncLoggerSetup.setup_logger(name, level, log_file)