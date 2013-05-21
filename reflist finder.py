from urllib.request import urlopen
import re

def wikitextGrabber(pageName):
    URL = "http://en.wikipedia.org/w/api.php?format=json&action=query&titles="+pageName+"&prop=revisions&rvprop=content"
    print (URL)
    
    rawtext = urlopen(URL)
    text = str(rawtext.readline())
    print (text)
    text = text.split('\\n')
    #print (text)
    return text

def findReflist(pageName):
    text =  wikitextGrabber(pageName)
    #print (text)
    for line in text:
        #print (line)
        matchObjTemplate = re.search(r'\{{2}[Rr]eflist\}{2}', line)
        matchObjTag = re.search(r'\<[Rr]eferences*\\\>', line)
        if matchObjTemplate:
           print (line)
           return True
        else:
           next
    else:
         return False

f = open("articles list.txt", 'r')
#files = f.read()
for line in f:
    line = str(line)
    #print (line)
    refFound = findReflist(line)
    if refFound == True:
       print ("References found in",line)
    else:
       print ("No references found in",line)
f.close()