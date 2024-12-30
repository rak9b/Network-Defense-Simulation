
from scapy.all import sniff
import logging
from typing import Callable, List, Dict
import json
from datetime import datetime


class IDSMonitor:
    """
    A class to monitor network traffic and detect suspicious activity based on IDS rules.
    """

    def __init__(self, rules_path: str):
        """
        Initialize the IDSMonitor with a rules configuration file.

        :param rules_path: Path to the IDS rules configuration file.
        """
        self.rules_path = rules_path
        self.logger = logging.getLogger(__name__)
        self.rules = self._load_rules()
        self.alerts = []

    def _load_rules(self) -> List[Dict]:
        """
        Load IDS rules from the configuration file.

        :return: A list of rules as dictionaries.
        """
        try:
            with open(self.rules_path, 'r') as file:
                rules = json.load(file)
                self.logger.info(f"Successfully loaded {len(rules)} rules from {self.rules_path}.")
                return rules
        except FileNotFoundError:
            self.logger.error(f"Rules file not found: {self.rules_path}")
            return []
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format in {self.rules_path}: {e}")
            return []
        except Exception as e:
            self.logger.error(f"Unexpected error while loading rules: {e}")
            return []

    def _matches_rule(self, packet, rule: Dict) -> bool:
        """
        Check if a packet matches a specific IDS rule.

        :param packet: The packet to analyze.
        :param rule: The rule to match against.
        :return: True if the packet matches the rule, False otherwise.
        """
        try:
            protocol = rule.get("protocol", "any")
            if protocol != "any" and packet.haslayer(protocol) is False:
                return False

            if "conditions" in rule:
                conditions = rule["conditions"]
                if conditions.get("port") and str(packet.dport) != str(conditions["port"]):
                    return False

            return True
        except AttributeError:
            return False

    def packet_callback(self, packet):
        """
        Analyze a packet and trigger alerts if it matches any rule.

        :param packet: The captured network packet.
        """
        for rule in self.rules:
            if self._matches_rule(packet, rule):
                alert = {
                    "timestamp": datetime.now().isoformat(),
                    "source": packet[0][1].src,
                    "destination": packet[0][1].dst,
                    "rule_matched": rule["name"],
                }
                self.alerts.append(alert)
                self.logger.warning(f"Alert triggered: {alert}")

    def start_monitoring(self, interface: str = "eth0"):
        """
        Start monitoring network traffic.

        :param interface: The network interface to capture packets on.
        """
        try:
            sniff(iface=interface, prn=self.packet_callback, store=0)
        except Exception as e:
            self.logger.error(f"Failed to start monitoring: {e}")
