# log_analyzer.py
# Project: Automated Log Anomaly Detector (Simulated Brute-Force Detection)

FAILURE_THRESHOLD = 4
LOG_FILE = 'simulated_logs.txt'

# Dictionary to store the count of failed logins for each IP
failed_attempts = {}

def analyze_logs():
    """Reads the log file and checks for IPs exceeding the failure threshold."""
    print("--- Starting Log Analysis ---")
    
    try:
        with open(LOG_FILE, 'r') as f:
            for line in f:
                # Assuming log format: TIME,IP,STATUS
                parts = line.strip().split(',')
                if len(parts) < 3:
                    continue
                
                timestamp, ip_address, status = parts[0].strip(), parts[1].strip(), parts[2].strip()
                
                if status == 'FAIL':
                    # Increment the failure count for this IP
                    failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1
                    
                    # CHECK FOR ANOMALY
                    if failed_attempts[ip_address] >= FAILURE_THRESHOLD:
                        # SIMULATED ALERT OUTPUT
                        print(f"\n🚨 **SECURITY ALERT** 🚨 (Brute Force Detected)")
                        print(f"Time: {timestamp}")
                        print(f"Source IP: {ip_address}")
                        print(f"Reason: Failed login count exceeded {FAILURE_THRESHOLD} attempts.")
                        
                        # Reset the count after alerting to avoid repetitive alerts
                        failed_attempts[ip_address] = 0 

                elif status == 'SUCCESS' and ip_address in failed_attempts:
                    # Clear failure counter upon successful login
                    failed_attempts[ip_address] = 0
                    
    except FileNotFoundError:
        print(f"Error: Log file '{LOG_FILE}' not found. Please create it.")
        
    print("\n--- Analysis Complete ---")

if __name__ == "__main__":
    analyze_logs()