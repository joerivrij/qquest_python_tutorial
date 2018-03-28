#!/usr/bin/env python


import os


files = os.listdir(os.curdir)
for file in files:
    if file.endswith(".txt"):
        os.rename(file, 'anothertest.xml')
        print(file)
    elif file.endswith(".xml"):
        os.rename(file, 'test.txt')
        print(file)

