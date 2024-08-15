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
        line = line.split()
        if len(line) > 2:
            counter += 1
            if counter <= 10:
                status = line[-2]
                file_size = line[-1]
                accumulated_data["File size"] += file_size
                if status in accumulated_data:
                    accumulated_data[status] += 1

            if counter == 10:
                print_stats(accumulated_data)
                counter = 0
finally:
    print_stats(accumulated_data)
