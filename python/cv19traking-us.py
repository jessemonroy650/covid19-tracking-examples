#!/usr/bin/python
#
#   2020-03-22T23:06:06
#   grab covid19 dataset from https://covidtracking.com/api/
#
import json
import urllib2

online_dataset = 'https://covidtracking.com/api/us'

filedata    = urllib2.urlopen(online_dataset)
datatowrite = filedata.read()
t           = datatowrite.decode()
#print  t
python_obj  = json.loads(t)
dataObject  = python_obj[0]
for k in sorted(dataObject):
    print dataObject[k], k

print ""
print "negative", dataObject['negative']

print "\ndone."

