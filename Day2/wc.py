from sys import argv,exit
import os.path

print("argvLen:", len(argv))
# print(argv[0])

def count(file_path):
    """count the line, word, and char of a given file"""
    line_count = 0
    word_count = 0
    char_count = 0

    # with open(file_path, mode="r", encoding="utf8") as file:
    f= open(file_path,'r')
    print("file opened")
    for line in f:
        line_count += 1
        char_count += len(line)
        word_count += len(line.split())
    f.close()
    return line_count, word_count, char_count


if len(argv) < 2:
    print("***ERROR: not enough arguments")
    exit(1)
else:
    for i in range(1, len(argv)):
        print("file path:", argv[1])
        # if not os.path.isfile(argv[1]):
        if not os.path.exists(i):
            print("file not exists:", i)
        else:
            # l, w, c = count(i)
            # print("l:", l, "\tw:", w, "\tc:", c, "\tf:", i.split("\\")[-1])
            print("%sl %sw %sc " % count(i), "\tf:", i.split("\\")[-1])
    exit(0)
