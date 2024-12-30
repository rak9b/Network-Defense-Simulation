"""
Network Defense Simulation: Core Package

This package contains the main modules for managing the simulation, including:
- Firewall management
- Intrusion Detection System (IDS)
- Real-time monitoring utilities

Modules:
    - firewall: Manages firewall rules and configurations.
    - ids: Handles intrusion detection and alerting mechanisms.
    - monitoring: Provides threat monitoring and analysis.
    - utils: Common utilities for logging and configuration management.

Author:
    Your Name

Version:
    1.0.0
"""

# Define the package version
__version__ = "1.0.0"

# Import core components for easier access
from .firewall.firewall_manager import FirewallManager
from .ids.ids_monitor import IDSMonitor
from .monitoring.threat_monitor import ThreatMonitor

# Log initialization of the package
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"Network Defense Simulation package (v{__version__}) initialized.")
