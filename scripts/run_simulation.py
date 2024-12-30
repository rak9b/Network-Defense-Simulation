import os
import logging
from src.firewall.firewall_manager import FirewallManager
from src.ids.ids_monitor import IDSMonitor
from utils.log_handler import setup_logging

def main():
    """Main entry point for the Network Defense Simulation."""
    # Setup logging
    log_file = "logs/network_simulation.log"
    setup_logging(log_file=log_file, level=logging.INFO)

    logger = logging.getLogger(__name__)
    logger.info("Starting Network Defense Simulation...")

    # Load configuration paths
    firewall_config_path = os.path.join("config", "firewall_rules.conf")
    ids_config_path = os.path.join("config", "ids_rules.conf")

    # Initialize Firewall Manager
    logger.info("Initializing Firewall Manager...")
    firewall_manager = FirewallManager(firewall_config_path)
    firewall_manager.apply_rules()
    logger.info("Firewall rules applied.")

    # Initialize IDS Monitor
    logger.info("Initializing IDS Monitor...")
    ids_monitor = IDSMonitor(ids_config_path)
    try:
        ids_monitor.start_monitoring(interface="eth0")
    except KeyboardInterrupt:
        logger.info("Simulation stopped by user.")

if __name__ == "__main__":
    main()
