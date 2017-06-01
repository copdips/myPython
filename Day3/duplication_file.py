def printFile(fileIn):
    with open(fileIn, mode="r", encoding='utf8') as myFileIn :
        print(myFileIn.read())

def duplicate_file(overwrite=False, append=False,**args):
    """ deplicate file"""
    print("args:",args.keys())
    for i in args.keys():
        print(i,":",args[i])

    if not {"src","dst"} <= args.keys():
        print("src and dst are the mandatory params")
        exit(1)

    print("***duplicate file***")

    with open(args["src"], mode="r", encoding='utf8') as myOldFile:

        if overwrite:
            open_mode = "w+"
        else:
            open_mode = "a"

        with open(args["dst"], mode=open_mode, encoding='utf8') as myNewFile:
            myNewFile.writelines(myOldFile.readlines())

    print("oldFile :", args["src"])
    printFile(args["src"])

    print("newFile :", args["dst"])
    printFile(args["dst"])



try :
    my_args = [
    'src="133.txt",dst="2.txt"',
    'src="22txt",dst="1.txt"',
    ]
    # duplicate_file(my_args)
    print("eval:")
    for a in my_args:
        eval('duplicate_file(' + a + ')')
    # duplicate_file("1.txt","2.txt",overwrite=True)
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
