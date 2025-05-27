#!/usr/bin/python3
"""
This script reads stdin line by line, parses log entries,
and computes metrics for total file size and status code counts.
It prints statistics every 10 lines or upon a keyboard interruption (CTRL + C).
"""
import sys
import signal
import re # Import the re module for regular expressions

total_file_size = 0
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
line_count = 0

# Regular expression to match the log line format
# This is more robust than splitting by space
LOG_FORMAT_RE = re.compile(
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '  # IP Address
    r'\[(.*?)\] '                               # Date
    r'"GET /projects/260 HTTP/1.1" '            # Request path
    r'(\d{3}) '                                 # Status Code
    r'(\d+)$'                                   # File Size
)

def print_metrics():
    """
    Prints the current total file size and status code counts.
    Status codes are printed in ascending order if their count is greater than 0.
    """
    print(f"File size: {total_file_size}")
    # Sort status codes for ascending order printing
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count > 0:
            print(f"{code}: {count}")

def signal_handler(sig, frame):
    """
    Handles keyboard interruption (CTRL+C) by printing metrics and exiting.
    """
    print_metrics()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        match = LOG_FORMAT_RE.match(line)
        if not match:
            # Skip line if it doesn't match the expected format
            continue

        try:
            # Extract status code and file size from regex groups
            current_status_code = match.group(3)
            current_file_size = int(match.group(4))

            # Update total file size
            global total_file_size # Needed here because we are modifying the global variable
            total_file_size += current_file_size

            # Update status code counts
            if current_status_code in status_codes:
                status_codes[current_status_code] += 1

        except ValueError:
            # This should ideally be caught by regex failure, but good for robustness
            pass
        except IndexError:
            # This handles cases where regex might match partially but groups are missing
            pass

        if line_count % 10 == 0:
            print_metrics()

finally:
    # Ensure metrics are printed when the script finishes (e.g., EOF or normal exit)
    print_metrics()
