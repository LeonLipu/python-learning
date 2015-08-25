
from urllib2 import urlopen
import json
#import jsonpath
import jsonpath


class client:

    def getresponse(self):
        url = "https://api.myjson.com/bins/1leee"
        response = urlopen(url)
        data = response.read()
        somejson = json.loads(data)
        match = jsonpath.jsonpath(somejson, '$..title')
        print match

ob = client()
ob.getresponse()
