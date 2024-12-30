import unittest
from unittest.mock import patch, mock_open
from scapy.packet import Packet
from src.ids.ids_monitor import IDSMonitor


class TestIDSMonitor(unittest.TestCase):
    def setUp(self):
        """Set up an IDSMonitor instance with a mock rules path."""
        self.rules_path = "mock_ids_rules.json"
        self.monitor = IDSMonitor(self.rules_path)

    @patch("builtins.open", new_callable=mock_open, read_data='[{"name": "Rule1", "protocol": "tcp"}]')
    @patch("json.load", return_value=[{"name": "Rule1", "protocol": "tcp"}])
    def test_load_rules_success(self, mock_json_load, mock_open_file):
        """Test loading IDS rules from a valid configuration file."""
        rules = self.monitor._load_rules()
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules[0]["name"], "Rule1")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_rules_file_not_found(self, mock_open_file):
        """Test behavior when the IDS rules file is not found."""
        rules = self.monitor._load_rules()
        self.assertEqual(len(rules), 0)

    @patch("src.ids.ids_monitor.IDSMonitor._matches_rule", return_value=True)
    def test_packet_callback_alert(self, mock_matches_rule):
        """Test that an alert is triggered when a packet matches a rule."""
        packet = Packet()
        packet.src = "192.168.1.5"
        packet.dst = "10.0.0.1"
        self.monitor.rules = [{"name": "TestRule"}]
        self.monitor.packet_callback(packet)
        self.assertEqual(len(self.monitor.alerts), 1)
        self.assertEqual(self.monitor.alerts[0]["rule_matched"], "TestRule")


if __name__ == "__main__":
    unittest.main()
