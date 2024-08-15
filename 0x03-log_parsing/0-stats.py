#!/usr/bin/python3
"""
script parses log data and calculates statistics based on the log entries.
The script reads log entries from the standard input and processes each line.
It expects log entries in the following format:
<IP> - [<Timestamp>] "GET /projects/260 HTTP/1.1" <Status Code> <File Size>
-The script accumulates data for each log entry
  and calculates the following statistics:
  - File size: The total file size of all log entries.
  - 200: The number of log entries with a status code of 200.
  - 301: The number of log entries with a status code of 301.
  - 400: The number of log entries with a status code of 400.
  - 401: The number of log entries with a status code of 401.
  - 403: The number of log entries with a status code of 403.
  - 404: The number of log entries with a status code of 404.
  - 405: The number of log entries with a status code of 405.
  - 500: The number of log entries with a status code of 500.
After processing 10 log entries, the script prints
the accumulated statistics and resets the counters.
Example usage:
  $ cat access.log | python3 0-stats.py
"""
import sys
import signal
import re


accumulated_data = {"File size": 0, "200": 0, "301": 0,
                    "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
counter = 0

try:
    for line in sys.stdin:
        # Remove trailing newline
        line = line.strip()
        # Process the line
        counter = 0
        if re.match(r"\d+\.\d+\.\d+\.\d+ - \[.*\] \
          \"GET /projects/260 HTTP/1.1\" \d+ \d+", line):
            data = line.split()
            if len(data) > 2:
                counter += 1
                status = data[-2]
                file_size = data[-1]
                accumulated_data["File size"] += int(file_size)
                if status in accumulated_data:
                    accumulated_data[status] += 1
        else:
            continue
        
        if counter == 10:
            print("File size: {}".format(accumulated_data["File size"]))
            for key, value in accumulated_data.items():
                if key != "File size" and value != 0:
                    print("{}: {}".format(key, value))
            counter = 0
            accumulated_data = {"File size": 0, "200": 0, "301": 0,
                                "400": 0, "401": 0, "403": 0,
                                "404": 0, "405": 0, "500": 0}
finally:
        print("File size: {}".format(accumulated_data["File size"]))
        for key, value in accumulated_data.items():
            if key != "File size" and value != 0:
                print("{}: {}".format(key, value))
