import logging
import os
from datetime import datetime
from typing import Optional, Dict, List, Union


class LoggerSetup:
    _instances: Dict[str, logging.Logger] = {}

    @classmethod
    def setup_logger(
            cls,
            name: str = __name__,
            level: int = logging.INFO,
            log_file: Optional[Union[str, List[str]]] = None,
            debug: bool = False
    ) -> logging.Logger:
        """
        Configure and return a logger instance that can be used across the project.
        """
        if name not in cls._instances:
            logger = logging.getLogger(name)
            # 디버그 모드일 경우 DEBUG 레벨로 설정
            logger.setLevel(logging.DEBUG if debug else level)

            if not logger.handlers:
                # 디버그용 상세 포맷터
                debug_formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
                )
                # 일반 포맷터
                normal_formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                )

                # 콘솔 핸들러 설정
                stream_handler = logging.StreamHandler()
                stream_handler.setFormatter(debug_formatter if debug else normal_formatter)
                logger.addHandler(stream_handler)

                if log_file:
                    os.makedirs('logs', exist_ok=True)
                    log_files = [log_file] if isinstance(log_file, str) else log_file

                    for file_prefix in log_files:
                        # 일반 로그 파일
                        normal_file_handler = logging.FileHandler(
                            f'logs/{file_prefix}_{datetime.now().strftime("%Y%m%d")}.log'
                        )
                        normal_file_handler.setFormatter(normal_formatter)
                        normal_file_handler.setLevel(level)
                        logger.addHandler(normal_file_handler)

                        if debug:
                            # 디버그 로그 파일
                            debug_file_handler = logging.FileHandler(
                                f'logs/{file_prefix}_debug_{datetime.now().strftime("%Y%m%d")}.log'
                            )
                            debug_file_handler.setFormatter(debug_formatter)
                            debug_file_handler.setLevel(logging.DEBUG)
                            logger.addHandler(debug_file_handler)

            cls._instances[name] = logger

        return cls._instances[name]


def get_logger(
        name: str = __name__,
        level: int = logging.INFO,
        log_file: Optional[Union[str, List[str]]] = None,
        debug: bool = False
) -> logging.Logger:
    return LoggerSetup.setup_logger(name, level, log_file, debug)