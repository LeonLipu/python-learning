class parent(object):
    def __init__(self):
        print "this parent construnctor "
    def fun1(self):
        print "this is parent function"

class child(parent):
    def __init__(self):
        print "this child construnctor"
        super(child,self).__init__()
    def fun2(self):
        print "this is child method "
ob=child()
ob.fun1()
ob.fun2()

#here parent must inherit from object and super(child ,self ).__init__() both are mandotory
