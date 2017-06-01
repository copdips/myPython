from sys import argv, exit, exc_info
from os.path import *
import zipfile
from os import mkdir,listdir,walk,makedirs
import os
from shutil import rmtree,copyfile




def newFolderByExtension(folder_path):
    """ create a new folder and group the files by extension """
    new_folder_path = folder_path + "_sorted"
    print("new_folder_path:", new_folder_path)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            print(file)
            print(root)
            print(dirs)
            file_ext = splitext(file)[1].strip(".")
            if file_ext == "":
                file_ext = "NoExtension"
            sub_folder = join(new_folder_path,file_ext)
            if not exists(sub_folder):
                print("new sub fodler:", sub_folder)
                makedirs(sub_folder)
                if not exists(sub_folder):
                    print("not created:",sub_folder)
            copyfile(file,join(sub_folder,file))

argv_len = len(argv)

if argv_len == 1:
    print("missing zipfile to extract")
    exit(1)
elif argv_len > 2:
    print("exactly one argument expected")
    exit(2)
else:
    if not isfile(argv[1]):
        print("file nout found:", argv[1])
        exit(3)
    else:
        file_fullname = basename(argv[1])
        file_name = splitext(file_fullname)[0]
        file_extension = splitext(file_fullname)[1]

        print("file_name:",file_name)
        print("file_extension:",file_extension)

        if file_extension.lower() != ".zip":
            print("zipfile expected")
            exit(4)
        else:
            if "corrompu" in file_name.lower():
                print("corrupted zipfile")
                exit(5)
            else:
                print("good zipfile:", argv[1])
                with zipfile.ZipFile(argv[1]) as myzip:

                    dest_path = splitext(argv[1])[0]
                    print("dest_path:",dest_path)

                    if exists(dest_path):
                        print("destination path exists, delete it")
                        rmtree(dest_path)

                    print("unzipping", argv[1])
                    myzip.extractall(path=dest_path)
                    print("unzip done")

                    newFolderByExtension(dest_path)





