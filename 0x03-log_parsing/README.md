0x03. Log Parsing
Project Overview
This project, part of the ALX interview preparation, focuses on parsing and processing log data streams in Python. The goal is to read log lines from standard input (stdin) in real-time, extract relevant metrics, and compute statistics. The script processes logs in a specific format, calculates the total file size, and counts occurrences of HTTP status codes, printing statistics every 10 valid lines or upon a keyboard interrupt (CTRL+C).
Requirements

Environment: Ubuntu 20.04 LTS
Python Version: Python 3.4.3
Allowed Editors: vi, vim, emacs
Code Style: PEP 8 (version 1.7.x), enforced using pycodestyle
Files:
All files must be executable (chmod +x)
First line: #!/usr/bin/python3
Must end with a newline


Dependencies: No external packages required (uses standard library: sys, re, signal, collections)

Task Description
Task 0: Log Parsing

File: 0-stats.py
Description: A Python script that reads log lines from stdin, computes metrics, and prints statistics.
Input Format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Skips lines that don’t match this format or have non-integer status codes/file sizes.


Metrics:
Total file size: Sum of all valid <file size> values.
Status code counts: Counts for status codes (200, 301, 400, 401, 403, 404, 405, 500) that appear.


Output:
Printed every 10 valid lines or on CTRL+C.
Format:File size: <total size>
<status code>: <count>

Status codes are printed in ascending order, only for those with counts > 0.


Testing: Use the provided 0-generator.py to simulate log input:./0-generator.py | ./0-stats.py



Setup and Usage

Clone the Repository:
git clone <your-repo-url>
cd alx-interview/0x03-log_parsing


Ensure Python 3.4.3:
python3.4 --version

If not installed:
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.4


Make Files Executable:
chmod +x 0-stats.py 0-generator.py


Run the Script:
./0-generator.py | ./0-stats.py


Expected output: Statistics every 10 lines (e.g., File size: 5213, 200: 2, etc.).
Press CTRL+C to see final stats.


Check Code Style:
pip install pycodestyle==1.7.1
pycodestyle 0-stats.py



Files

0-stats.py: Main script for parsing logs and computing metrics.
0-generator.py: Provided script for generating test log data.
README.md: This file, describing the project and usage.

Example Output
Running ./0-generator.py | ./0-stats.py might produce:
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3

On CTRL+C:
File size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4

Notes

The script handles invalid lines by skipping them.
Only valid status codes (200, 301, 400, 401, 403, 404, 405, 500) are counted.
The project was completed as part of the ALX interview preparation, with a deadline of May 9, 2025.

Author
[Kale Francis]
License
This project is for educational purposes as part of the ALX program.
