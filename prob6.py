'''
Created on Nov 13, 2015

@author: apple
'''
#!/usr/bin/env python2
import urllib
import pickle

page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(page) # read the lists of tupples in file 
page.close()

print data,"\n"
#data: [('char',number),,,][(),,,]
#print number times character char to find final result
#ex: [('a',2),('b',3)] -> aabbb
# 1 list = 1 line

for lst in data:
    print "".join([item[1] * item[0] for item in lst])