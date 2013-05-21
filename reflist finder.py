from urllib.request import urlopen
import re

def wikitextGrabber(pageName):
    URL = "http://en.wikipedia.org/w/api.php?format=json&action=query&titles="+pageName+"&prop=revisions&rvprop=content"
    #print (URL)
    
    rawtext = urlopen(URL)
    text = str(rawtext.readline())
    text = text.split('\\n')
    return text

def findReflist(pageName):
    text =  wikitextGrabber(pageName)
    #print (text)
    for line in text:
        #print (line)
        matchObj = re.search(r'\{{2}[Rr]eflist\}{2}', line)
        if matchObj:
           print (line)
           return True
        else:
           next
    else:
         return False

refFound = findReflist("Sophia_Smith")
if refFound == True:
   print ("Woohoo!")
else:
   print ("Boo :(")