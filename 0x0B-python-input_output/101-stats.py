#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys

def print_metrics(total_size, status_codes):
    """Print the accumulated metrics."""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 6:
                # Assuming the format is correct, extract relevant parts
                status_code = int(parts[-2])  # status code is the second last part
                file_size = int(parts[-1])     # file size is the last part

                # Update total size and status codes
                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        # On keyboard interrupt, print metrics
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
