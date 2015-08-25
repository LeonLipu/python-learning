
from urllib2 import urlopen
import json
from jsonpath_rw import jsonpath, parse


class client:

    def getresponse(self):
        url = "https://api.myjson.com/bins/1leee"
        response = urlopen(url)
        data = response.read()
        jsonexpression =parse("$..glossary")
        dataarray=[match.value for match in jsonexpression.find(data)]
        #dataarray=jsonexpression.find(data);
        #print dataarray
        dataparse=[match.value for match in parse('foo[*].id').find({'foo': [{'id': 'bizzle'}, {'baz': 3}]})]
        print dataparse

        #print data


ob = client()
ob.getresponse()
