# Automated Log Analyzer

## Overview

This Automated Log Analyzer scans and processes log files to detect security threats and anomalies.

Features

Parses log files from system logs, web servers, or custom sources.

Detects suspicious activity (e.g., failed SSH logins, HTTP errors).

Configurable alert rules using config.json.

Prerequisites

Python 3.x


# Clone the repository
git clone https://github.com/yourusername/Automated-Log-Analyzer.git
cd Automated-Log-Analyzer

# Install dependencies (if any, currently none)
pip install -r requirements.txt

# Usage

Running the Log Analyzer

python3 src/log_analyzer.py

Modifying Alert Rules

Edit config.json to define custom log file paths and alert patterns.

# Notes

Ensure logs/sample.log exists before running the script.

Modify config.json to analyze different logs.

# License

This project is licensed under the MIT License.

