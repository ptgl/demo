'''
Created on Oct 24, 2015

@author: apple
'''
import re

f = open("dataProb4.txt", "r+")
str = f.read();
#the pattern: 
#1 character that is not a capital letter
#3 capital letters
#1 lower case letter
#3 capital letters
#1 character that is not a capital letter.
#print re.findall("([^A-Z])+[A-Z]{3}([a-z])([A-Z]{3})[^A-Z]+", str)
print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", str))
# Close opend file
f.close()