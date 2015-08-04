
# A script that renames files.

# open the location where the files are.
# get the file names.
# check the file names.
# for each file, rename the files if they match the criteria.
import os


# import os imports the whole module and thus needing to use the function method
# os.listdir
# from os import listdir one can simply use the function.

def rename_files():
    #(1) get file names from a folder
    # will return everything in that directory as a list.
    file_list = os.listdir('/home/teichopsia/venv_python/prog_foundations/prank')
    print(file_list)
    
    saved_path = os.getcwd()
    print("Current working directory is: " + saved_path)
    
    os.chdir('/home/teichopsia/venv_python/prog_foundations/prank')
    
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New name - " + file_name.translate(None, "0123456789"))
        #         old files -> to new file names.
        os.rename(file_name, file_name.translate(None, "0123456789"))
    
    os.chdir(saved_path) #change the path back to how it was.
    
    # string.translate(s, table[, deletechars])
    # import string
    # to_replace = "1234567890"
    # string.translate(file_name, None, to_replace)
    # is equivalent to:
    # file_name.translate(None, to_replace)
    
rename_files()
