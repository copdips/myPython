#!/usr/bin/env python3
from sys import argv, exit
from os.path import exists

def counting(filename):
    nLines = nWords = nChars = 0
    with open(filename,'r') as f:
        for line in f:
            nLines += 1
            nChars += len(line)
            nWords += len(line.split())

    return nLines, nWords,nChars

if len(argv) < 2:
    print('Not enough arguments!')
    exit(1)

else:
    for filename in argv[1:]:
        if exists(filename):
            l,w,c = counting(filename)
            print('Lines:', l, ' - Words:', w, ' - Chars:', c, "for file:" ,filename)
        else:
            print("file not found: ", filename)





