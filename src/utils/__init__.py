"""
Utility Module

This module contains common utilities used across the Network Defense Simulation project.

Modules:
    - log_handler: Provides a standardized logging setup for the project.

Author:
    Your Name

Version:
    1.0.0
"""

from .log_handler import setup_logging

# Define the package version
__version__ = "1.0.0"

__all__ = ["setup_logging"]
