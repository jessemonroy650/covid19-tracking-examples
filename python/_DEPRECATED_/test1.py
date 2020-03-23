#!/usr/bin/python
#
#	test grab covid19 dataset from https://covidtracking.com/api/
#
import json

import urllib2

filedata = urllib2.urlopen('https://covidtracking.com/api/us')
datatowrite = filedata.read()

#print datatowrite
#print json.load(datatowrite)
#print json.dumps(datatowrite)

t = datatowrite.decode()
print  t

#json_data = '{"name": "Brian", "city": "Seattle"}'
python_obj = json.loads(t)
pp = python_obj[0]
for k in pp:
    print pp[k], k

#print pp['negative']
#print python_obj["city"]


#with open('path_to_file/person.json') as f:

#data = json.load(datatowrite)

#print(data)

print "done."

