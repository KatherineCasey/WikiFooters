from urllib.request import urlopen
import re



def wikitextGrabber(pageName):
    pageName = pageName.strip()
    URL = "http://en.wikipedia.org/w/api.php?format=json&action=query&titles="+pageName+"&prop=revisions&rvprop=content"

    rawtext = urlopen(URL)
    text = str(rawtext.readline())
    text = text.split('\\n')
    #print (text)
    return text

def findReflist(pageName):
    text =  wikitextGrabber(pageName)
    #print (text)
    for line in text:
        #print (line)
        matchObjTemplate = re.search(r'\{{2}[Rr]eflist', line)
        matchObjTag = re.search(r'\<[Rr]eferences', line)
        if matchObjTemplate or matchObjTag:
           print (line)
           return True
        else:
           next
    else:
         return False

def findExternalLinks(pageName):
    pass

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