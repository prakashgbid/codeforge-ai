"""
auto-coder
=============

A powerful Python package extracted from OSA.
"""

__version__ = "0.1.0"
__author__ = "OSA Contributors"

from .core import AutoCoder
from .exceptions import AutoCoderError

__all__ = [
    "AutoCoder",
    "AutoCoderError",
]
