#!/usr/bin/python
#
#   2020-03-22T23:06:06
#   grab covid19 dataset from https://covidtracking.com/api/
#
import json
import urllib2

data_encoding = 'utf-8'

u = online_dataset = 'https://covidtracking.com/api/urls'

filedata    = urllib2.urlopen(online_dataset)
datatowrite = filedata.read()
t           = datatowrite.decode(data_encoding)
#print  t
python_obj  = json.loads(t)
dataObject  = python_obj[0]
for k in sorted(dataObject):
    print dataObject[k], k

print "\ndone."

