from os import listdir
from os import rename
from os import getcwd
from os import chdir

def rename_files():

    # (1) get file names from a folder    
    file_list = listdir(r"F:\folder")
    print(file_list)

    # (2) for each file, rename filename
    saved_path = getcwd()
    print("Current Working Directory is " + saved_path)
    chdir(r"F:\folder")    
    for file_name in file_list:
        new_filename = file_name.translate(None, "0123456789")
        print(file_name + " -> " + new_filename)
        rename(file_name, new_filename)
    chdir(saved_path)
    
rename_files()
