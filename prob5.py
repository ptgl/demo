'''
Created on Oct 24, 2015

@author: apple
'''
import urllib, re, time

result = "27709"

 
while True:
    source = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + result) #open page
    text = source.read()
    number = re.findall(r'\d+', text) # find the number at the end of URL
    result = "".join(number)
    if result == "": # if the end of URL is not number -> result
        print text
        break
    else:
        print result
        