#!/usr/bin/python3
"""This module contains the solution for the log parsing problem"""
# from sys import stdin


# def print_status_codes(code):
#     """Prints the status code with its count.
#     Format:
#         <status>: <count>
#     """
#     for key, val in sorted(code.items()):
#         print("{}: {}".format(key, val))


# code = {}
# file_size = 0
# vals_total = 0

# try:
#     for line in stdin:
#         line = line.split()
#         file_size += int(line[-1])
#         status = int(line[-2])
#         vals = list(code.values())
#         vals_total = sum(vals)

#         if not status or type(status) != int:
#             continue

#         if vals_total % 10 == 0:
#             if code:
#                 print("File size: {}".format(file_size))
#                 print_status_codes(code)

#         if status not in code:
#             code[status] = 1  
#         else:
#             code[status] += 1

#         vals_total += 1
        
# except KeyboardInterrupt:
#     pass
#     # print_status_codes(code)

import sys
from collections import defaultdict

def print_statistics(file_size, status_counts):
    print("File size: {}".format(file_size))
    for status, count in sorted(status_counts.items()):
        print("{}: {}".format(status, count))

def main():
    file_size = 0
    status_counts = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            parts = line.split()
            
            # Ensure the line matches the expected format
            if len(parts) != 9 or parts[6].isdigit() is False:
                continue
            
            status_code = int(parts[6])
            file_size += int(parts[8])
            status_counts[status_code] += 1
            
            if i % 10 == 0:
                print_statistics(file_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(file_size, status_counts)

if __name__ == "__main__":
    main()
