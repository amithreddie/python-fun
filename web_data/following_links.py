# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
    
while count >= 0:
    print "Retrieving:", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[pos-1].get('href', None)
            
    
    count = count - 1