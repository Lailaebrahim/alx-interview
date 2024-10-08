#!/usr/bin/python3
"""
Script parses log data and calculates statistics based on the log entries.
The script reads log entries from the standard input and processes each line.
It expects log entries in the following format:
<IP> - [<Timestamp>] "GET /projects/260 HTTP/1.1" <Status Code> <File Size>
The script accumulates data for each log entry and calculates statistics.
After processing 10 log entries, the script prints the accumulated statistics.
"""

import sys
import re

# Regular expression pattern for log entry format
LOG_FORMAT = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) - \[(.+)\] "GET /projects/260 HTTP/1\.1" '
    r'(\d+) (\d+)'
)
accumulated_data = {"File size": 0, "200": 0, "301": 0,
                    "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
counter = 0


def print_stats(data):
    """Print accumulated statistics"""
    print(f"File size: {data['File size']}")
    for key, val in sorted(data.items()):
        if key != "File size" and val > 0:
            print(f"{key}: {val}")


try:
    for line in sys.stdin:
        match = LOG_FORMAT.match(line.strip())
        if match:
            counter += 1
            if counter <= 10:
                status = match.group(3)
                file_size = int(match.group(4))
                accumulated_data["File size"] += file_size
                if status in accumulated_data:
                    accumulated_data[status] += 1

            if counter == 10:
                print_stats(accumulated_data)
                counter = 0
finally:
    print_stats(accumulated_data)
