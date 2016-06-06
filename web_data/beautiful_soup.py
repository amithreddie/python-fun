# Instructions here: https://pr4e.dr-chuck.com/tsugi/mod/python-data/index.php?PHPSESSID=f43514813233b4b30e299c1f9575ace6
# Scraping Numbers from HTML using BeautifulSoup In this assignment you will 
# write a Python program similar to http://www.pythonlearn.com/code/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, and 
# parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you 
# the sum for your testing and the other is the actual data you need to process for 
# the assignment.

# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_282735.html (Sum ends with 0)

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of span tags
spans = soup('span')
total = 0
for span in spans:
    total = total + int(span.contents[0])
print total