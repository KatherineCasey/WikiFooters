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
    
def findSection(text,regex):
    sectionLoc = 'none'
    sectionIden = regex
    for index in range(0,len(text)-1):
        matchSection = re.search(sectionIden, text[index])
        if matchSection:
           match = True
           sectionLoc = index
           break
    else:
         match = False
    return match, sectionLoc

def findReflist(text):
    refsLoc = 'none'
    refsTemplateIden = (r'\{{2}[Rr]eflist')
    refsTagIden = (r'\<[Rr]eferences')
    for index in range(0,len(text)-1):
        matchRefs = re.search(refsTemplateIden or refsTagIden, text[index])
        if matchRefs:
           match = True
           refsLoc = index
           break
    else:
         match = False
    return match, refsLoc

def findExternalLinks(text):
    #determine whether an EL section is present, and find its location
    extLinkLoc = 'none'
    linkIden = re.compile(r'==[eE]xternal [Ll]inks')
    for index in range(0,len(text)-1):
        matchLinks = re.search(linkIden, text[index])
        if matchLinks:
           extLinkLoc = index
           match = True
           break
    else:
         match = False
    return match, extLinkLoc

def findCategories(text):
    catLoc = 'none'
    catIden = re.compile(r'\[\[[cC]ategory')
    for index in range(0,len(text)-1):
        matchCats = re.search(catIden, text[index])
        if matchCats:
           catLoc = index
           match = True
           break
    else:
           match = False
    return match, catLoc
  
def findWorks(text):
    worksLoc = 'none'
    worksIden = re.compile(r'== *(Works *==|Bibliography|Publications|Source)')
    ographiesIden = re.compile(r'ography *==')
    for index in range(0,len(text)-1):
        matchWorks = re.search(worksIden or ographiesIden, text[index])
        if matchWorks:
           worksLoc = index
           match = True
           break
    else:
           match = False
    return match, worksLoc

def findSeeAlso(text):
    seeLoc = 'none'
    seeIden = re.compile(r'== *See [Aa]lso')
    for index in range(0,len(text)-1):
        matchSee = re.search(seeIden, text[index])
        if matchSee:
           seeLoc = index
           match = True
           break
    else:
           match = False
    return match, seeLoc

f = open("articles list.txt", 'r')

refsTemplateIden = re.compile(r'\{{2}[Rr]eflist')
refsTagIden = re.compile(r'\<[Rr]eferences')
linkIden = re.compile(r'==[eE]xternal [Ll]inks')
catIden = re.compile(r'\[\[[cC]ategory')
worksIden = re.compile(r'== *(Works *==|Bibliography|Publications|Source)')
ographiesIden = re.compile(r'ography *==')
seeIden = re.compile(r'== *See [Aa]lso')

#files = f.read()
for line in f:
    line = str(line)
    print (line)
    text = wikitextGrabber(line)

    print ("Reflist?",findReflist(text))
    print ("External Links?", findSection(text, linkIden))
    print ("Categories?", findSection(text, catIden))
    print ("Works?", findWorks(text))
    print ("See Also?", findSection(text, seeIden))
    print ("---------")
f.close()