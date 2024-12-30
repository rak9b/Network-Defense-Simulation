"""
Intrusion Detection System (IDS) Module

This module provides functionality for monitoring network traffic and detecting
suspicious activity based on predefined rules.

Classes:
    - IDSMonitor: Analyzes packets and triggers alerts for suspicious activity.

Author:
    Your Name

Version:
    1.0.0
"""

from .ids_monitor import IDSMonitor

# Define the package version
__version__ = "1.0.0"

__all__ = ["IDSMonitor"]
