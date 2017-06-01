def printFile(fileIn):
    with open(fileIn, mode="r", encoding='utf8') as myFileIn :
        print(myFileIn.read())

def duplicate_file(src,dst,overwrite=False, append=False):
    """ deplicate file"""

    print("***duplicate file***")

    with open(src, mode="r", encoding='utf8') as myOldFile:

        if overwrite:
            open_mode = "w+"
        else:
            open_mode = "a"

        with open(dst, mode=open_mode, encoding='utf8') as myNewFile:
            myNewFile.writelines(myOldFile.readlines())

    print("oldFile :", src)
    printFile(src)

    print("newFile :", dst)
    printFile(dst)



try :
    duplicate_file("1.txt","2.txt")
    duplicate_file("1.txt","2.txt",overwrite=True)
    # duplicate_file("1.mp3","2.mp3",overwrite=True)
except TypeError as e:
    print("TypeError:", e)
except NameError as e:
    print("NameError:", e)
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
except UnicodeDecodeError as e:
    print("UnicodeDecodeError", e)
else:
    print("i'm else")
finally:
    print("i'm finally")