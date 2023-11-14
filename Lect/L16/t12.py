import os

current_folder_content = os.listdir(path=".")
# print(current_folder_content)
f_name = "todel.txt"
if f_name in current_folder_content:
    print(f"file {f_name} has been removed")
    os.remove(f_name)