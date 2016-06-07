# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to 
# http://www.pythonlearn.com/code/json2.py. The program will prompt for a 
# URL, read the JSON data from that URL using urllib and then parse and 
# extract the comment counts from the JSON data, compute the sum of the 
# numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we 
# give you the sum for your testing and the other is the actual data you 
# need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_282736.json (Sum ends with 71)

import json
import urllib

url = raw_input('Enter location: ')
if len(url)<1:
    url = 'http://python-data.dr-chuck.net/comments_42.json'
total = 0
try:
    print 'Retrieving ', url
    input = urllib.urlopen(url).read()
    info = json.loads(input)
except:
    print "Error loading data."
    
print 'Retrieved', len(input), 'characters'

for item in info['comments']:
    total = total + int(item['count'])

print total