
#it is class name
class abc:
    #it is contructor and prameterised
  def __init__(self,x,y):
    self.y=y
    self.x=x

# this is method need to implimeted
  def get (self):
   print self.x

#object creation
ob =abc(88,99);
ob.get();
