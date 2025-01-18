from importlib.metadata import metadata

from .calculator import Calculator
from .main import main

_package_metadata = metadata(str(__package__))
__version__ = _package_metadata["Version"]
__author__ = _package_metadata.get("Author-email", "")

__all__ = ["Calculator", "__author__", "__version__", "main"]
