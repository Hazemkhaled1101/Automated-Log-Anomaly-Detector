#  Automated Log Anomaly Detector (Brute-Force Simulation)

## Project Overview

This project simulates a core function of a **Security Operations Center (SOC)**: real-time analysis and detection of anomalous behavior within log data. The Python script processes a static log file (`simulated_logs.txt`) and flags potential brute-force attacks by monitoring the rate of failed login attempts from source IP addresses.

### Key Skills Demonstrated

* **Detection Engineering:** Defining and implementing security monitoring rules (4 failed logins = alert).
* **Log Analysis:** Parsing unstructured log data using Python.
* **Incident Triage:** Identifying high-priority, high-volume threats like brute-force activity.
* **Python for Security:** Using dictionaries and loops for efficient data processing.

---

## How It Works

The `log_analyzer.py` script utilizes a simple counting mechanism:

1.  It maintains a dictionary mapping **Source IP Address** to its current **Failed Login Count**.
2.  For every log line with a `FAIL` status, the count for that IP is incremented.
3.  If the count meets or exceeds the defined `FAILURE_THRESHOLD` (set to **4**), a simulated `SECURITY ALERT` is generated, and the count for that IP is reset.

---

## Running the Project

1.  Ensure you have **Python 3** installed.
2.  Save the `log_analyzer.py` and `simulated_logs.txt` files in the same directory.
3.  Execute the script from your terminal:

```bash
python log_analyzer.py