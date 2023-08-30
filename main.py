# importing essential modules
import os   # importing os module


# identifying paths and other variables
directory_path = "TestFolder"   # the host directory path
total_files = 0 # number of total files in the host directory

fd_list = os.listdir(directory_path)    # list of files and directories

# counting the total number of files
for file_name in fd_list:
    if "." in file_name:
        total_files += 1

print(total_files)