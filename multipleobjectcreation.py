
#it is class name
class abc:
    #it is contructor and prameterised
  def __init__(self,x,y):
    self.y=y
    self.x=x

# this is method need to implimeted
  def get (self):
   print self.x
   print "class abc is included"

#object creation
ob =abc(88,99);
ob.get();

class xyz :
    def get(self):
        print "class xyz is included"

print "*****************declaring object for multiple class*****************"

combinedObject= [abc(77,66),xyz()]

for ob in combinedObject:
    print ob.get()
