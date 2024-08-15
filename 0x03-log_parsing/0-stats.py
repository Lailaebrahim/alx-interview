import sys
import signal
import re


accumulated_data = {"File size": 0, "200": 0, "301": 0,
                    "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
for line in sys.stdin:
    # Remove trailing newline
    line = line.strip()

    # Process the line
    if re.match(r"\d+\.\d+\.\d+\.\d+ - \[.*\] \"GET /projects/260 HTTP/1.1\" \d+ \d+", line):
        data = line.split()
        if len(data) > 1:
            status = data[-2]
            file_size = data[-1]
            accumulated_data["File size"] += int(file_size)
            if status in accumulated_data:
                accumulated_data[status] += 1
    else:
        continue
