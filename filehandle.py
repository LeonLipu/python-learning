
# os related function
import os

#this is for reading
file =open('file.txt','r')
print file.name,file.closed
read= file.read()
print read
file.close()

#this is for writing
wfile =open('w.txt','w')
wfile.close()



print os.environ
print os.getcwd()
print os.geteuid()
