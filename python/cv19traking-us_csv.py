#!/usr/bin/python
#
#   2020-03-23T01:57:41
#   grab covid19 dataset from https://covidtracking.com/api/
#
import csv
import urllib2

online_dataset = 'https://covidtracking.com/api/us.csv'

filedata  = urllib2.urlopen(online_dataset)
apireader = csv.reader(filedata, delimiter=' ', quotechar='|')

print next(apireader)
print '----'

for r in apireader:
    print r

print "\ndone."
exit



