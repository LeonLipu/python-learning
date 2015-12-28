#here is list tutorial of list

# it is similar to array list

list1 =["lipu","is","handsomeguy","and","he","not","solution","something"]

print list1

print "****** accessing value ********";
print "list[0] is ",list1[0]
print "list[1:3]",list1[1:3]
print "*************deleting *********** "
del list1[0]
print "after deleting list[0] is ", list1


print "***********some basic operation ************"
print len(list1) # length of list
print [1,2,3]+[4,5,6] # concatenation
print ["hi"]*5 #multipication
print 3 in [1,3,4] #contains method
for x in [1,2,3]:print x #iteration


print "**********some built in method and functions ************"

print "*************cmp method **********"
list1,list2=[123,'xyz'],[456,'abc']
print cmp(list1,list2) # if arg1>arg2 return 1 if arg1<arg2 return return -1 and arg1==arg2 return 0

print max([123,321,33,112,324]) # and there is min

print "****how to convert touple to list ********"

touple =("hello","hi","something")
print list(touple) #here list as constructor so never list keywork as variable

print "***********some of object method with obejct **************"
list3=["hello","something","nothing","hello"]
list3.append("everything")
print "after appending ",list3
print list3.count("hello") # no of occurrance of object in list
list1,list2=[1,2],[3,4]
list1.extend(list2)
print list1
print list1.index(2)
list1.insert(3,2222)
print list1
list1.pop()
print list1 # we can give pop(1) and 1 is counted from last
list1.remove(2222)
print list1
list1.reverse()
print list1
list1.sort()
print list1


# ***********some of object method with obejct **************
# after appending  ['hello', 'something', 'nothing', 'hello', 'everything']
# 2
# [1, 2, 3, 4]
# 1
# [1, 2, 3, 2222, 4]
# [1, 2, 3, 2222]
# [1, 2, 3]
# [3, 2, 1]
# [1, 2, 3]
