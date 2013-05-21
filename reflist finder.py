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
    match = False
    if len(regex) == 0:
       print ("Error: You must specify at least one regular expression to be compiled.")
    else:
        for index in range(0,len(text)-1): #for every line in the text
             for spot in regex:      #for every regex provided
                 arg = re.compile(spot)
                 matchSection = re.search(arg, text[index])   #see if that regex is in the text
                 if matchSection: #if it is...
                    match = True  #set match to True
                    sectionLoc = index #mark the location of the regex match
                    break  #exit the regex loop
                 else:  #if there's no regex match...
                    next #try the next regex
             if match == True:
                break
        else: #if you never hit a True condition in the checking the text for the regexes
             match = False  #set match to False
    return match, sectionLoc

f = open("articles list.txt", 'r')

refsTemplateIden = r'\{{2}[Rr]eflist'
refsTagIden = r'\<[Rr]eferences'
linkIden = r'==[eE]xternal [Ll]inks'
catIden = r'\[\[[cC]ategory'
worksIden = r'== *(Works *==|Bibliography|Publications|Source)'
ographiesIden = r'ography *=='
seeIden = r'== *See [Aa]lso'

for line in f:
    line = str(line)
    print (line)
    lineattributes = {}
    text = wikitextGrabber(line)
    lineattributes['reflist'] = findSection(text, refsTemplateIden, refsTagIden)
    lineattributes['external_links'] = findSection(text, linkIden)
    lineattributes['categories'] =  findSection(text, catIden)
    lineattributes['works'] = findSection(text, worksIden, ographiesIden)
    lineattributes['see_also'] = findSection(text, seeIden)
    for item in lineattributes:
        if lineattributes[item][1] == "none":
           print ("No", item, "found.")
        else:
           entry = int(lineattributes[item][1])
           print (item, "at location", lineattributes[item], text[entry])
    print ("--------")
f.close()