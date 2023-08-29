import os

file_count = 0
dir_path = "E:\Test"

for file_path in os.scandir(dir_path):
    if file_path.is_file():
        file_count += 1

file_name = os.path.splitext(os.path.basename('/root/file.ext'))
print(file_name)
