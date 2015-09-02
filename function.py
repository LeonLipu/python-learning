
#it happens in functional programming 
def expon(element,n):
    if(n==0):

        return 1
    else:
        return element*expon(element,n-1)

print expon(5,3)
