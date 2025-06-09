#!/usr/bin/python3
"""
This script is a shebang line for a python script that generates random log entries.
"""

import sys
import signal

status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_file_size = 0
line_count = 0

def print_metrics():
    """
    This function will be responsible for printing the current metrics
    """
    print(f"File size: {total_file_size}")
    for status_code, count in status_codes.items():
        if count > 0:
            print(f"{status_code}: {count}")

def signal_handler(sig, frame):
    """
    This function will be called when CTRL+C is pressed.
    """
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        
        try:
            parts = line.split()
            if len(parts) < 9:
                continue

            current_status_code = parts[-2]
            current_file_size = int(parts[-1])
            global total_file_size
            total_file_size += current_file_size
            global status_counts
            if current_status_code in status_counts:
                status_counts[current_status_code] += 1
                
        except ValueError:
            pass

        if line_count % 10 == 0:
            print_metrics()
finally:
    # Ensure metrics are printed when the script finishes (e.g., EOF or normal exit)
    print_metrics()
