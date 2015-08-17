
from urllib2 import urlopen
import json
class client:
    def getresponse(self):
        url ="https://api.myjson.com/bins/2xqto"
        response=urlopen(url)
        data= response.read()
        print data



ob = client();
ob.getresponse();
