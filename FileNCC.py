# importing essential modules
import os   # importing os module
import itertools


# identifying paths and other variables
host_path = os.getcwd() # gets the current directory path
directory_path = input("Host directoreh: ").replace(" ", "_")   # the host directory path
# total_files = 0 # number of total files in the host directory
user_input = input("Name format: ").replace(" ", "_")
old_list = []
new_list = []

fd_list = os.listdir(directory_path)    # list of files and directories


# counting the total number of files
for file_num, file_name in enumerate(fd_list):
    # if "." in file_name:    # it will ignore the directories in the host directory
    #     total_files += 1

    # identify the code from user input
    if "N+N" in user_input:
        new_file_name = host_path + "\\" + directory_path + "\\" + user_input.replace("N+N", str(file_num+1))

    # will look into this feature later
    # generate decreasing numbers
    """
    elif "N-N" in user_input:
        new_file_name = host_path + "\\" + directory_path + "\\" + user_input.replace("N-N", str(abs(len(fd_list) - (total_files+1))))
    """
    
    # generating the existing files' paths
    file_directory = host_path + "\\" + directory_path + "\\" + file_name
    new_file_directory = new_file_name.replace("_", " ")

    # storing old and new paths and file names
    old_list.append(file_directory)
    new_list.append(new_file_directory)


# changing the file names
for (old_name, new_name) in zip(old_list, new_list):
    os.rename(old_name, new_name)
