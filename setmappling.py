import os
print "hello warld "

def name():
    print "myname "

def child():
    print "something"

class abc:
    def getname(self):
        print "getnamefunction"
    def setname(self,name):
        print "this is setname"+name
        print os.getpid()
        pid=os.fork()
        if pid==0:
            child()
        else :
            print "parent process is running "


ob=abc()
ob.getname()
ob.setname("lipu")
