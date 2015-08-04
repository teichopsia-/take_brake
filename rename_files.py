
# A script that renames files.

# open the location where the files are.
# get the file names.
# check the file names.
# for each file, rename the files if they match the criteria.
import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir('/home/teichopsia/venv_python/prog_foundations/prank') # will return everything in that directory
    print(file_list)
    #(2) for each file, rename filename
    
rename_files()
