#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text 
#and numbers. You will extract all the numbers in the file and compute 
#the sum of the numbers.

#Data Files
#We provide two files for this assignment. One is a sample file where 
#we give you the sum for your testing and the other is the actual data 
#you need to process for the assignment.

#Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There 
#are 87 values with a sum=445822)
#Actual data: http://python-data.dr-chuck.net/regex_sum_282730.txt 
#(There are 92 values and the sum ends with 246)

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_282730.txt"
handle = open(name)
result = 0
nums = list()
for line in handle:
    strnums = re.findall('[0-9]+', line)
    if len(strnums) > 0: 
        for num in strnums:
            result = result + int(num)
print result