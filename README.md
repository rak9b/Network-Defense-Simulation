
# Network Defense Simulation

A comprehensive network defense simulation environment incorporating firewalls, IDS/IPS systems, and real-time threat monitoring. This project is designed to simulate real-world scenarios to enhance your understanding of network security.

---

## Features

- **Firewall Management**:
  - Configurable firewall rules using `iptables`.

- **Intrusion Detection System (IDS)**:
  - Real-time network traffic analysis using custom rules.

- **Alert System**:
  - Logs alerts for suspicious activities detected in network traffic.

- **Seamless Integration**:
  - Compatible with tools like Wireshark, Snort, and Splunk for extended analysis.

---

## Getting Started

### Prerequisites

Ensure the following are installed on your system:

- Python 3.8 or higher
- `pip` (Python package manager)
- Administrative privileges for configuring `iptables`

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/username/network-defense-sim.git
    cd network-defense-sim
    ```

2. **Set Up the Environment**:
    Run the setup script to create a virtual environment, install dependencies, and initialize configurations.
    ```bash
    bash scripts/setup.sh
    source venv/bin/activate
    ```

3. **Verify Installation**:
    Ensure all dependencies are installed successfully:
    ```bash
    python -m pip list
    ```

---

## Usage

### Starting the Simulation

1. **Run the Simulation**:
    ```bash
    python scripts/run_simulation.py
    ```

2. **Monitor Logs**:
    Check logs for real-time activities and alerts:
    ```bash
    tail -f logs/network_simulation.log
    ```

### Testing

Run the test suite to verify functionality:
```bash
pytest tests/
```

---

## Directory Structure

```plaintext
network-defense-sim/
├── README.md                     # Documentation
├── requirements.txt              # Python dependencies
├── config/                       # Configuration files
├── scripts/                      # Utility scripts
├── src/                          # Core application code
├── tests/                        # Unit tests
└── logs/                         # Log files (generated dynamically)
```

---

## Configuration

### Firewall Rules (`config/firewall_rules.conf`)
Define rules for the firewall in JSON format:
```json
[
    {"source": "192.168.1.0/24", "destination": "10.0.0.0/24", "protocol": "tcp"}
]
```

### IDS Rules (`config/ids_rules.conf`)
Define rules for the intrusion detection system:
```json
[
    {"name": "BlockSSH", "protocol": "tcp", "port": 22}
]
```

---

## Dependencies

The project uses the following Python libraries:
- `scapy`: For packet sniffing and analysis
- `python-iptables`: For managing firewall rules
- `pytest`: For running unit tests
- `python-json-logger`: For structured logging
- `splunk-sdk`: For potential integration with Splunk

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to the open-source community for providing tools like `scapy` and `python-iptables`.

For questions or contributions, feel free to open an issue or a pull request on the repository.
```

---

### **`requirements.txt`**
```plaintext
scapy>=2.4.5
python-iptables>=1.0.0
pytest>=6.2.5
python-json-logger>=2.0.2
splunk-sdk>=1.6.18
```

---
