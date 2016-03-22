#dictionary nothing but key-value pair and keys should be immutable object and can not modified
dict ={'name':'brahmanda','age':'27'}
print dict['name'],dict['age']
dict['add']='kolkota' #adding new key
print dict
dict.clear()
print "after clear" ,dict

dic ={'name':"gandhi",'age':77}
print "********length"
print len(dic)
print str(dic)
print "********type "
print type(dic) #return type of variable that passed into it
dic2=dic.copy()
print dic2
print "********forming dic from tuple "
sq=('p1','p2')
dic3=dict.fromkeys(sq,'something')
print dic3
print "********geting value "
print dic.get("sex",'male')
print "******** has key"
print dic.has_key('sex')
print "*********** items "
print dic.items()
print "*********** keys  "
print dic.keys()
print "set default ",dic.setdefault('age',None)
print "set default ",dic.setdefault('height ',None)
dic2 ={'add':'kol'}
dic.update(dic2)
print "after update ", dic
print "getting value " ,dic.values()


print "inverting "


m ={'a':1,'b':2,'c':3}

print m.items()

print

mi = dict(zip(m.values(),m.keys()))
