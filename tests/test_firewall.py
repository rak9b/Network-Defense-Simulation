import unittest
from unittest.mock import patch, mock_open
from src.firewall.firewall_manager import FirewallManager


class TestFirewallManager(unittest.TestCase):
    def setUp(self):
        """Set up a FirewallManager instance with a mock configuration path."""
        self.config_path = "mock_firewall_rules.json"
        self.manager = FirewallManager(self.config_path)

    @patch("builtins.open", new_callable=mock_open, read_data='[{"source": "192.168.1.0/24", "destination": "10.0.0.0/24", "protocol": "tcp"}]')
    @patch("json.load", return_value=[{"source": "192.168.1.0/24", "destination": "10.0.0.0/24", "protocol": "tcp"}])
    def test_load_rules_success(self, mock_json_load, mock_open_file):
        """Test loading firewall rules from a valid configuration file."""
        rules = self.manager._load_rules()
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules[0]["source"], "192.168.1.0/24")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_rules_file_not_found(self, mock_open_file):
        """Test behavior when the configuration file is not found."""
        rules = self.manager._load_rules()
        self.assertEqual(len(rules), 0)

    @patch("iptc.Chain.insert_rule")
    def test_apply_rules(self, mock_insert_rule):
        """Test applying firewall rules with iptables."""
        self.manager.rules = [
            {"source": "192.168.1.0/24", "destination": "10.0.0.0/24", "protocol": "tcp"}
        ]
        self.manager.apply_rules()
        self.assertTrue(mock_insert_rule.called)


if __name__ == "__main__":
    unittest.main()
