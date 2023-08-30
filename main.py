# importing essential modules
import os   # importing os module


# identifying paths and other variables
host_path = os.getcwd()
directory_path = "TestFolder"   # the host directory path
total_files = 0 # number of total files in the host directory
user_input = "Fight Club S01EN+N.txt"

fd_list = os.listdir(directory_path)    # list of files and directories


# counting the total number of files
for file_name in fd_list:
    if "." in file_name:    # it will ignore the directories in the host directory
        total_files += 1

    if "N+N" in user_input:
        new_file_name = host_path + "\\" + directory_path + "\\" + user_input.replace("N+N", str(total_files))
    elif "N-N" in user_input:
        new_file_name = host_path + "\\" + directory_path + "\\" + user_input.replace("N-N", str(total_files))
    
    file_directory = host_path + "\\" + directory_path + "\\" + file_name

    os.rename(file_directory, new_file_name)
