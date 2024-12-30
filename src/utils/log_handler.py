import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logging(log_file: str = "app.log", level: int = logging.INFO, max_bytes: int = 5 * 1024 * 1024, backup_count: int = 3):
    """
    Sets up logging for the application with a rotating file handler and console output.

    :param log_file: Path to the log file.
    :param level: Logging level (default: logging.INFO).
    :param max_bytes: Maximum size of the log file in bytes before rotation (default: 5MB).
    :param backup_count: Number of backup log files to retain (default: 3).
    """
    # Ensure the directory for the log file exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a rotating file handler
    file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

    # Get the root logger and add handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    logging.info(f"Logging initialized. Log file: {log_file}")


if __name__ == "__main__":
    # Example usage of the logging setup
    setup_logging(log_file="logs/app.log", level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info("This is an info message.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
