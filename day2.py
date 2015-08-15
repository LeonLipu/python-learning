import re

line =" there is my mail box is there "

obj = re.match(r'.*',line, re.I|re.M)
print obj.group()


def concat():
    print "this is function"
    pass
concat();
