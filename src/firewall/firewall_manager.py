import logging
import json
from typing import List, Dict
import iptc

class FirewallManager:
    """
    Manages firewall rules using iptables.

    Attributes:
        config_path (str): Path to the firewall configuration file.
        logger (logging.Logger): Logger for debugging and error reporting.
        rules (List[Dict]): Loaded firewall rules from the configuration file.
    """

    def __init__(self, config_path: str):
        """
        Initializes the FirewallManager.

        Args:
            config_path (str): Path to the firewall configuration file.
        """
        self.config_path = config_path
        self.logger = logging.getLogger(__name__)
        self.rules = self._load_rules()

    def _load_rules(self) -> List[Dict]:
        """
        Load firewall rules from the configuration file.

        Returns:
            List[Dict]: List of firewall rules.

        Logs:
            Error if the configuration file fails to load or parse.
        """
        try:
            with open(self.config_path, 'r') as f:
                rules = json.load(f)
            self.logger.info("Firewall rules loaded successfully.")
            return rules
        except FileNotFoundError:
            self.logger.error(f"Configuration file not found: {self.config_path}")
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse JSON: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error while loading rules: {e}")
        return []

    def apply_rules(self):
        """
        Apply firewall rules using iptables.

        Logs:
            Info for successfully applied rules.
            Errors for any failures in applying rules.
        """
        for rule in self.rules:
            try:
                chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
                rule_obj = iptc.Rule()

                # Set rule parameters
                rule_obj.src = rule.get('source', '0.0.0.0/0')
                rule_obj.dst = rule.get('destination', '0.0.0.0/0')
                rule_obj.protocol = rule.get('protocol', 'tcp')

                # Match protocol-specific parameters (e.g., port)
                if 'port' in rule and rule['port'] != "any":
                    match = rule_obj.create_match(rule_obj.protocol)
                    match.dport = rule['port']

                # Set target action
                target = rule.get('action', 'DROP')
                rule_obj.target = iptc.Target(rule_obj, target)

                # Insert the rule
                chain.insert_rule(rule_obj)
                self.logger.info(f"Applied rule: {rule['name']}")
            except Exception as e:
                self.logger.error(f"Failed to apply rule '{rule.get('name', 'Unnamed')}': {e}")

    def list_rules(self) -> List[Dict]:
        """
        List currently loaded firewall rules.

        Returns:
            List[Dict]: A list of current firewall rules.
        """
        return self.rules

    def flush_rules(self):
        """
        Flush all rules in the INPUT chain.

        Logs:
            Info for successful flush.
            Errors for any failures.
        """
        try:
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
            chain.flush()
            self.logger.info("All INPUT chain rules have been flushed.")
        except Exception as e:
            self.logger.error(f"Failed to flush rules: {e}")
