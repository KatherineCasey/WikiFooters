from urllib.request import urlopen
import re



def wikitextGrabber(pageName):
    pageName = pageName.strip()
    URL = "http://en.wikipedia.org/w/api.php?format=json&action=query&titles="+pageName+"&prop=revisions&rvprop=content"

    rawtext = urlopen(URL)
    text = str(rawtext.readline())
    text = text.split('\\n')
    return text
    #returns a list of the lines in the text, split at newline

def findReflist(text, pageName):
    #text =  wikitextGrabber(pageName)
    #print (text)
    for line in text:
        #print (line)
        matchObjTemplate = re.search(r'\{{2}[Rr]eflist', line)
        matchObjTag = re.search(r'\<[Rr]eferences', line)
        if matchObjTemplate or matchObjTag:
           print ("References found in",pageName)
           return True
        else:
           next
    else:
         print ("No references found in", pageName)
         return False

def findExternalLinks(text):
    extLinkLoc = 'none'
    linkIden = re.compile(r'[eE]xternal [Ll]inks')
    for index in range(0,len(text)-1):
        matchLinks = re.search(linkIden, text[index])
        if matchLinks:
           extLinkLoc = index
           match = True
           return [match, extLinkLoc]
        else:
           next
    else:
         match = False
         return [match, extLinkLoc]  

f = open("articles list.txt", 'r')
#files = f.read()
for line in f:
    line = str(line)
    #print (line)
    text = wikitextGrabber(line)
    if findReflist(text, line):
       print (line)
       matchFound = findExternalLinks(text)[0]
       print (matchFound)
       matchLoc = findExternalLinks(text)[1]
       print (matchLoc)
       print ('---------')
    else:
       next
f.close()