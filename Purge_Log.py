#!/bin/python3

import shutil   # for file copy
import os       # for get_file_size and check if the file exists
import sys      # for CLI arguments

# example: my_log.txt 10 (max size), 5 (max file amount)

if len(sys.argv) < 4:
    print("Missing arguments!  Usage is script.py 10 5")
    exit(1)

file_name   = sys.argv[1]
limit_size  = int(sys.argv[2])
logs_number = int(sys.argv[3])

if os.path.isfile(file_name):                   # Check if main logfile file exists
    logfile_size = os.stat(file_name).st_size   # Get file size in BYTES
    logfile_size = logfile_size / 1024          # Convert from BYTES to KILOBYTES

    if logfile_size >= limit_size:
        if logs_number > 0:
            for current_file_number in range(logs_number, 1, -1):
                src = file_name + "_" + str(current_file_number-1)
                dst = file_name + "_" + str(current_file_number)
                if os.path.isfile(src):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + "  to  " + dst)

            shutil.copyfile(file_name, file_name + "_1")
            print("Copied " + file_name + "  to  " + file_name + "_1")
        my_file = open(file_name, 'w')
        my_file.close()
