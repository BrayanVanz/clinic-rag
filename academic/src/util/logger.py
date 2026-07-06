"""This module provides a utility function to set up a logger for a given module name."""

from pathlib import Path
import logging
import sys

def setup_logger(name_of_module: str) -> logging.Logger:
  """
  Configures and returns a logger for the specified module name.
  
  :param name_of_module: The name of the module for which the logger is being set up.
  :return: Configured logger instance.
  """

  logger = logging.getLogger(name_of_module)

  logger.setLevel(logging.INFO)

  if logger.hasHandlers():
    return logger
  
  formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
  )

  # === Create logs directory if it doesn't exist === 

  Path("logs").mkdir(parents=True, exist_ok=True)
  file_handler = logging.FileHandler(f"logs/{name_of_module}.log", encoding="utf-8")
  file_handler.setFormatter(formatter)
  
  # === Create logs for console === 

  console_handler = logging.StreamHandler(sys.stdout)
  console_handler.setFormatter(formatter)

  # === Create the Handlers for Directory & Console ===

  logger.addHandler(file_handler)
  logger.addHandler(console_handler)

  return logger
  