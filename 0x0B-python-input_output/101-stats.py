#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Displays statistics of total lines read after:
    - Reading 10 lines
    - Keyboard interruption (CTRL + c)

Output format:
    -Total file size: File size: <total size>
     where <total size>  is the sum of all previous (see input format above)
    - Number of lines by status code:
    - Possible status code:
         > 200, 301, 400, 401, 403, 404, 405, 500
    - If a status code doesn’t appear,
      nothing is printed for the status code format: <status code>: <number>
    - Status codes are printed in ascending order
"""
import sys


def display_stats(total_size, stats):
    """
    Displays summary of the stats read from stdin.
    Args:
        total_size (int): The total file size read.
        stats (dict): The dictionary with summary of status codes totals
    """
    print("Total file size: {}".format(total_size))
    sorted_stats = sorted(stats.items(), key=lambda x: int(x[0]))
    for key, value in sorted_stats:
        print("{}: {}".format(key, value))


def parse_line(line):
    status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_parts = line.split()
    try:
        line_size = int(line_parts[-1])
        status_code = line_parts[-2]
        is_valid_code = status_code in status_codes
        return {
            "line_size": line_size,
            "status_code": status_code,
            "is_valid_code": is_valid_code
        }
    except (IndexError, ValueError):
        return None


def read_from_stdin():
    line_count = 0
    total_size = 0
    stats = {}
    try:
        for line in sys.stdin:
            line_count += 1
            parsed_data = parse_line(line)
            if parsed_data is not None:
                total_size += parsed_data["line_size"]
                if parsed_data["is_valid_code"]:
                    stats[parsed_data["status_code"]] = stats.get(parsed_data["status_code"], 0) + 1
            if line_count % 10 == 0:
                display_stats(total_size, stats)
    except KeyboardInterrupt:
        display_stats(total_size, stats)
        raise


if __name__ == "__main__":
    read_from_stdin()
