#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Count of status codes (200, 301, 400, 401, 403, 404, 405, 500)
Prints metrics every 10 lines and on keyboard interruption.
"""

import sys
import re

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

# Regex pattern to match exact format
log_pattern = re.compile(
    r'^(\d+\.\d+\.\d+\.\d+) - \[.+?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)

def print_metrics():
    """Prints the current file size and status code counts."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        match = log_pattern.match(line.strip())
        if match:
            status_code, file_size = match.group(2), match.group(3)
            try:
                total_file_size += int(file_size)
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                continue

        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    raise
finally:
    print_metrics()
