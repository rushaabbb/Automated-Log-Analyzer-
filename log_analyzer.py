import re
import json

def load_config(config_file="config.json"):
    """Load configuration settings from JSON file."""
    with open(config_file, 'r') as file:
        return json.load(file)

def analyze_log(log_file, alert_patterns):
    """Scan log file for suspicious patterns."""
    with open(log_file, 'r') as file:
        logs = file.readlines()
    
    alerts = []
    for line in logs:
        for pattern, description in alert_patterns.items():
            if re.search(pattern, line):
                alerts.append(f"Alert: {description} -> {line.strip()}")
    
    return alerts

def main():
    config = load_config()
    log_file = config["log_file"]
    alert_patterns = config["alert_patterns"]
    
    print("[+] Analyzing logs...")
    alerts = analyze_log(log_file, alert_patterns)
    
    if alerts:
        print("\n".join(alerts))
    else:
        print("[+] No suspicious activity detected.")

if __name__ == "__main__":
    main()
