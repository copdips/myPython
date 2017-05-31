def printFile(fileIn):
    with open(fileIn, mode="r", encoding='utf8') as myFileIn :
        print(myFileIn.read())

def duplicateFile(*a):
    print()
    print("***duplicate file")
    if len(a) == 2:
        with open(a[0], mode="r", encoding='utf8') as myOldFile:
            with open(a[1], mode="w+", encoding='utf8') as myNewFile:

                myNewFile.writelines(myOldFile.readlines())

        print("oldFile :", a[0])
        printFile(a[0])

        print("newFile :", a[1])
        printFile(a[1])
    elif len(a) == 3:
        print("receive dont eccrasement, nothing to do")
    else:
        print("please use 2 or 3 arguments")
        return None

duplicateFile("C:\\Users\\gk\\Documents\\myPython\\Day2\\old.txt", "C:\\Users\\gk\\Documents\\myPython\\Day2\\new.txt")

def cryptFile(fileIn, fileOut, shift):
    if shift == 3:
        print("Warning : offset is 3 which will have unexpected behavior on Windows for CRCL, nothing to do")
    else:
        print()
        print("***crypt file")
        print("fileIn path : ", fileIn)
        # print("fileIn content : ", end="")
        # printFile(fileIn)

        # print("===start crypt")
        print("shift :", shift)
        with open(fileIn, mode="r", encoding='utf8') as myfilein:
            with open(fileOut, mode="w+", encoding='utf8') as myFileOut:
                for aChar in myfilein.read() :
                    aCharCrypted = chr(ord(aChar)+int(shift))
                    # print(aChar, ord(aChar), "=> ", end="")
                    # print(aCharCrypted, ord(aCharCrypted))
                    myFileOut.write(aCharCrypted)
        # print("===end crypt")

        print("fileOut path : ", fileOut)
        # print("fileOut content : ", end="")
        # printFile(fileOut)

offset = 3

cryptFile("C:\\Users\\gk\\Documents\\myPython\\Day1\\gnuText.py", "C:\\Users\\gk\\Documents\\myPython\\Day2\\oldCrypted.txt", offset)

cryptFile("C:\\Users\\gk\\Documents\\myPython\\Day2\\oldCrypted.txt","C:\\Users\\gk\\Documents\\myPython\\Day2\\oldDecrypted", -offset)

print()
print("encoding :")
from sys import getdefaultencoding as enc_py
print(enc_py())

from sys import getfilesystemencoding as enc_sys
print(enc_sys())