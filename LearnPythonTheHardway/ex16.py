__author__ = 'viczmandni'
# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv # argumentum variables

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w') # file megnyitása írásra

print ("Truncating the file.  Goodbye!")
target.truncate() # a file tartalma törlésre kerül

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")   #
line2 = input("line 2: ")   # 3 sor bemenet
line3 = input("line 3: ")   #

print ("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n") # inputok összefűzése

print ("And finally, we close it.")
target.close() # file lezárása