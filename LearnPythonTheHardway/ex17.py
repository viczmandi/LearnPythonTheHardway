__author__ = 'viczmandni'
# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print ("The input file is %d bytes long" % len(indata)) # a file hossza byte-okban

print ("Does the output file exist? %r" % exists(to_file)) # a célfile létezik-e?
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') # cél file megnyitása írásra
out_file.write(indata) # bementi file  tartalmának beleírása a célfileba

print ("Alright, all done.")

out_file.close()
in_file.close()