class A(object):
    def __init__(self):
        print "constructor called "
class B(A):
    def __init__(self):
        super(B,self).__init__()
ob=B()
