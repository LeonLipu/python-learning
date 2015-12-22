
#variable declaration

var1 ="hello something "
var2 ="byfornothig"
print "***************** nomarl  value ************\n\n"
 #echo my value
print var2
print "var2 [0]",var2[0]  # here string is by default is array is replace ment of charat in javascript
print "var2[1:4]" ,var2[1:4] #it substring of java script and "," use for +

#for updateing string
print "***************** updating value ************\n\n"
print "updateing string ",var2[:3]+" new value " # it will cut first 2 value and update the string

#now we will learn about formatting
print "***************** formatting  ************\n\n"
print " my name is %s and age %d" %('Brahmanda',22)

#Now we will learn about some
print "***************** built in method  value  ************\n\n"
str1="brahmanada"
print str1.capitalize() #make first letter as capitalize

print str1.count('a',0,33) # no of occurances=(string to be searched ,initial index ,last index)

enstr=str1.encode('base64','strict') # encodeed string =(encode type ,mode)
print enstr
print enstr.decode('base64','strict') #decoded string =(endcode type ,mode )

print str1.endswith('da',0,22)  # yes/no =(string must  end with,string start from ,string end with  )
print str1.find('na',0) #index of element =(string to find ,start index ,end index ) if not find return s -1
print "123a".isalnum() # yes/no =if all member is number at least one
print "abca".isalpha() #yes/no =if all member is alphabate no numeric shoud be there
print "123".isdigit() # check for digit
print "abcd".islower()
