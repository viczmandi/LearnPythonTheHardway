__author__ = 'viczmandni'
# -*- coding: utf-8 -*-
from sys import argv # sys csomag, argv module

script, filename = argv # terminalban megadni a script nevét és file nevét
txt = open(filename)    # file megnyitása majd txt-be lementés

print ("Here's your file %r:" % filename) # file név kiíratása
print (txt.read()) # a txt változóban letárolt text file tartalmának kiírása

txt.close() # file lezárása olvasás után


"""
print ("Type the filename again:") #másik file név megadása
file_again = (input("> "))

txt_again = open(file_again)

print (txt_again.read())
"""