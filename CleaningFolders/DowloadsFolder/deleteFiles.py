import os

print("which file would you like to delete")
file_name=input()
file_path = '/Users/doual/Downloads/'+file_name

# Check if the file exists
if os.path.isfile(file_path):
    os.remove(file_path)
    print("The file has successfully been removed")
else: 
    print("This file hasn't been removed, as it doesn't exist")