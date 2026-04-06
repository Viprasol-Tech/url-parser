"""
url-parser - Parse and validate URLs

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import UrlParser, parse, process, main

__all__ = ["UrlParser", "parse", "process", "main"]
