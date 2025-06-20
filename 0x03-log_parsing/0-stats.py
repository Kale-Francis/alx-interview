#!/usr/bin/python3
"""
Script to parse log lines from stdin and compute metrics
"""
import sys
import re
import signal
from collections import defaultdict

# Regular expression to match the log format
LOG_PATTERN = re.compile(
    r'^(\S+) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)

# Valid status codes
VALID_STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize metrics
total_size = 0
status_counts = defaultdict(int)
line_count = 0


def print_stats():
    """Print current statistics"""
    print("File size: {}".format(total_size))
    for status in sorted(VALID_STATUS_CODES):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def signal_handler(sig, frame):
    """Handle keyboard interrupt (CTRL+C)"""
    print_stats()
    sys.exit(0)


# Set up signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
for line in sys.stdin:
    # Strip whitespace
    line = line.strip()
    
    # Match the log line format
    match = LOG_PATTERN.match(line)
    if not match:
        continue  # Skip invalid lines
    
    # Extract status code and file size
    try:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
    except ValueError:
        continue  # Skip if status code or file size is not an integer
    
    # Validate status code
    if status_code not in VALID_STATUS_CODES:
        continue
    
    # Update metrics
    total_size += file_size
    status_counts[status_code] += 1
    line_count += 1
    
    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final stats if there are remaining lines
if line_count % 10 != 0:
    print_stats()
