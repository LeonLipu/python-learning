
#lazy enumerate the list
favlist=['hello','my','darling']
print list(enumerate(favlist))

#for loop with enumeration
for i,fav in enumerate(favlist):
    print ("%d : %s" %(i,fav))
