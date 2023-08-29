import os


file_count = 0
dir_path = "TestFolder"
user_input = "HelloNN++"
   

# if "NN++" in user_input:
#     for file_path in os.scandir(dir_path):
#         if file_path.is_file():
#             file_count += 1
#             print(os.path.basename(dir_path))
        
        
for file_path in os.scandir(dir_path):
        if file_path.is_file():
            file_count += 1
            print(os.path.basename(dir_path))

# file_name = os.path.splitext(os.path.basename('/root/file.ext'))
# print(file_name)

# print(list(os.scandir(dir_path)))