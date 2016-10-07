#!/usr/bin/python

# Open a file
import re

file = open("dataProb3.txt", "r+")
str = file.read();
print "demo"
print re.findall("[A-Za-z]", str)
print "--".join(re.findall("[A-Za-z]", str))


# Close opend file
file.close()