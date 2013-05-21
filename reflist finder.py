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
    
def findSection(text, *regex):
    sectionLoc = 'none'
    #sectionIden = regex
    if len(regex) == 0:
       print ("Error: You must specify at least one regular expression to be compiled.")
    else:
        for index in range(0,len(text)-1):
             for spot in regex:
                 arg = re.compile(spot)
                 matchSection = re.search(arg, text[index])
                 if matchSection:
                    match = True
                    sectionLoc = index
                    break
        else:
             match = False
    return match, sectionLoc

f = open("articles list.txt", 'r')

refsTemplateIden = r'\{{2}[Rr]eflist'
refsTagIden = r'\<[Rr]eferences'
linkIden = r'==[eE]xternal [Ll]inks'
catIden = r'\[\[[cC]ategory'
worksIden = r'== *(Works *==|Bibliography|Publications|Source)'
ographiesIden = r'ography *=='
seeIden = r'== *See [Aa]lso'

#files = f.read()
for line in f:
    line = str(line)
    print (line)
    text = wikitextGrabber(line)

    print ("Reflist?",findSection(text, refsTemplateIden, refsTagIden))
    print ("External Links?", findSection(text, linkIden))
    print ("Categories?", findSection(text, catIden))
    print ("Works?", findSection(text, worksIden, ographiesIden))
    print ("See Also?", findSection(text, seeIden))
    print ("---------")
f.close()