import re

line ="once you have accomplished small thing succefully and you may 122 333 start greatone succufully"

obj = re.match(r'.*',line, re.I|re.M)
print obj.group()



print re.findall(r"\bs[\w]*",line)
it= re.finditer(r"\bs[\w]*",line)

print "**************************************************"
for match in it:
    print "{g} was found between in the indices {s}".format(g=match.group(),s=match.span())



print "*****************************************"
print re.split("\W+",line);


if(re.search("small",line)):
    print "search is sucessfully"

print re.sub("\d","",line)
