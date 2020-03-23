#!/usr/bin/python
#
#   2020-03-23T02:11:30
#   grab covid19 dataset from https://covidtracking.com/api/
#
import csv
import urllib2

data_encoding = 'utf-8'

u = online_dataset = 'https://covidtracking.com/api/us/daily.csv' #'https://covidtracking.com/api/us'

urls_dataset = [ 'https://covidtracking.com/api/us', 'https://covidtracking.com/api/us/daily', \
                 'https://covidtracking.com/api/counties', 'https://covidtracking.com/api/states', \
                 'https://covidtracking.com/api/states/daily'] # , 'https://covidtracking.com/api/states/info']

urls_dump_headers = ['US current', 'US daily',
                     'Counties', 'States current',
                     'States daily 4 pm ET','States info']

filedata  = urllib2.urlopen(online_dataset)
apireader = csv.reader(filedata, delimiter=' ', quotechar='|')

#
# NOTE: Once you pull date through the channel (socket) you CANNOT rewind.
#       However, you can pull down the entire file and process it.
#       The four (4) examples below show what you can do.
#

#######
## 1 ##
#######
# dump the header
#print "\nCSV labels\n"
#print next(apireader)
#exit()

#######
## 2 ##
#######
# dump the header & data
#print "\nCSV labels & data dump (row by row)\n"
#print next(apireader)
#print '----'
#for r in apireader:
#    print r
#exit()

#######
## 3 ##
#######
# get the length (minus the header)
#print "\nCSV number of data rows\n"
#apireader = csv.reader(filedata, delimiter=' ', quotechar='|')
#print u, "csv_data - length ", len(list(apireader)) - 1
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
print theFieldNames
for row in reader:
    print '++'
    print "date", row['date'], "\npositive", row['positive'], "\ndeath", row['death']

print "\ndone."
#exit()


