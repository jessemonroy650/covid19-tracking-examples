#!/usr/bin/python
#
#   2020-03-22T23:06:06
#   grab covid19 dataset from https://covidtracking.com/api/
#
import json
import urllib2

data_encoding = 'utf-8'

u = online_dataset = 'https://covidtracking.com/api/counties' #'https://covidtracking.com/api/us'

urls_dataset = [ 'https://covidtracking.com/api/us', 'https://covidtracking.com/api/us/daily', \
                 'https://covidtracking.com/api/counties', 'https://covidtracking.com/api/states', \
                 'https://covidtracking.com/api/states/daily'] # , 'https://covidtracking.com/api/states/info']

urls_dump_headers = ['US current', 'US daily',
                     'Counties', 'States current',
                     'States daily 4 pm ET','States info']

def get_dataset(url):
    return urllib2.urlopen(url).read()

def process_data(dd, de):
    return json.loads(dd.decode(de))

def dump_data(data):
    for aKey in sorted(data):
        print data[aKey], aKey

print "\n", urls_dump_headers[1], "\n"

d2 = get_dataset(u)
json_data = process_data(d2, data_encoding)
theLength = len(json_data)
print u, "json_data - length ", theLength
for i in range(0, theLength):
    print "\nINDEX ", i, "\n"
    print json_data[i]['county'], "\n"
    theD = json_data[i]
    dump_data(theD)
    
#
print "\ndone."
exit


