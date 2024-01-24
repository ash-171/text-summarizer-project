import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a yaml file and return a ConfigBox object.
    Args:
        path_to_yaml (str): Path to the yaml file.
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: A ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"yaml file: {path_to_yaml} could not be loaded")
        logger.error(f"error: {e}")
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories if they do not exist.
    Args:
        path_to_directories (list): List of path of directories to create.
        ignore_log(bool, optional): ignore if multiple dirs are to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.
    Args:
        path (Path): Path to the file.
    Returns:
        str: The size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"