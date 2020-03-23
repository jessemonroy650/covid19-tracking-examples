#!/usr/bin/python
#
#   2020-03-22T23:06:06
#   grab covid19 dataset from https://covidtracking.com/api/
#
import csv
import urllib2

data_encoding = 'utf-8'

u = online_dataset = 'https://covidtracking.com/api/states.csv' #'https://covidtracking.com/api/us'

urls_dataset = [ 'https://covidtracking.com/api/us', 'https://covidtracking.com/api/us/daily', \
                 'https://covidtracking.com/api/counties', 'https://covidtracking.com/api/states', \
                 'https://covidtracking.com/api/states/daily'] # , 'https://covidtracking.com/api/states/info']

urls_dump_headers = ['US current', 'US daily',
                     'Counties', 'States current',
                     'States daily 4 pm ET','States info']

filedata  = urllib2.urlopen(online_dataset)
apireader = csv.reader(filedata, delimiter=' ', quotechar='|')

#######
## 1 ##
#######
# dump the header
#print "\nCSV labels\n"
#print next(apireader)
#exit()


#######
## 4 ##
#######
# dump as a dictionary (automatically grabs header)
print "\nCSV dump as a dictionary (example)\n"
print '----'
reader = csv.DictReader(filedata)
# also this with Dictionary
theFieldNames = reader.fieldnames
for row in reader:
    print '++'
    for t in theFieldNames:
        print t, row[t]


print "\ndone."
exit()


