import os

current_folder_content = os.listdir(path=".")
print(current_folder_content)
f_name = "input10.txt"
if f_name in current_folder_content:
    f = open(f_name)
    print(f.read())
    f.close()