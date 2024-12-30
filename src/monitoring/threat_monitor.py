import logging
from typing import List, Dict
from datetime import datetime


class ThreatMonitor:
    """
    A class to monitor and aggregate threat activity detected by various components.
    """

    def __init__(self):
        """
        Initialize the ThreatMonitor.
        """
        self.logger = logging.getLogger(__name__)
        self.alerts = []

    def record_alert(self, alert: Dict):
        """
        Record a new threat alert.

        :param alert: A dictionary containing alert details.
        """
        self.alerts.append(alert)
        self.logger.info(f"New alert recorded: {alert}")

    def get_alert_summary(self) -> List[Dict]:
        """
        Get a summary of all recorded alerts.

        :return: A list of recorded alerts with timestamps and details.
        """
        return self.alerts

    def generate_report(self) -> str:
        """
        Generate a human-readable report of all recorded alerts.

        :return: A string containing the threat report.
        """
        report_lines = ["Threat Monitoring Report", "=" * 25]
        for alert in self.alerts:
            report_lines.append(f"[{alert['timestamp']}] Rule Matched: {alert['rule_matched']}")
            report_lines.append(f"    Source: {alert['source']}")
            report_lines.append(f"    Destination: {alert['destination']}")
            report_lines.append("-" * 25)
        return "\n".join(report_lines)


if __name__ == "__main__":
    # Example usage
    logging.basicConfig(level=logging.INFO)
    monitor = ThreatMonitor()

    # Simulate an alert
    monitor.record_alert({
        "timestamp": datetime.now().isoformat(),
        "source": "192.168.1.5",
        "destination": "10.0.0.1",
        "rule_matched": "Ping Flood Detection"
    })

    print(monitor.generate_report())
