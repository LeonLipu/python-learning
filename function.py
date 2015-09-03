
#it happens in functional programming
def expon(element,n):
    if(n==0):

        return 1
    else:
        return element*expon(element,n-1)

print expon(5,3)


arr=[(lambda x:x*x)(x)  for x in range(10)]
print arr

def  f(n):
    for i in range(n):
        yield i**3


for x in f(5):
    print x
