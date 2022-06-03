import os
import time

days = 5
folders = ["D:\\"]

total_deleted_size  = 0
total_deleted_files = 0
total_deleted_dirs  = 0

current_time = time.time()
age_time = current_time - 60*60*24*days


def delete_old_files(folder):
    """Delete files older than X days"""
    global total_deleted_files
    global total_deleted_size
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)
            file_time = os.path.getmtime(file_name)
            if file_time < age_time:
                size_file = os.path.getsize(file_name)
                total_deleted_size += size_file
                total_deleted_files += 1
                print("Deleting file: " + str(file_name))
                os.remove(file_name)


def delete_empty_dirs(folder):
    global total_deleted_dirs
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            total_deleted_dirs += 1
            empty_folders_in_this_run += 1
            print("Deleting empty dirs: " + str(path))
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_dirs(folder)


# ---------------------------MAIN--------------------------#

start_time = time.asctime()

for folder in folders:
    delete_old_files(folder)
    delete_empty_dirs(folder)

finish_time = time.asctime()

print("--------------START---------------")
print("Start time: "                    + str(start_time))
print("Total deleted size: "            + str(int(total_deleted_size / 1024 / 1024)) + "MB")
print("Total deleted files: "           + str(total_deleted_files))
print("Total deleted empty folders: "   + str(total_deleted_dirs))
print("Finish time: "                   + str(finish_time))
print("--------------FINISH--------------")
