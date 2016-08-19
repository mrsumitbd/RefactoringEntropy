# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 12:30:29 2016

@author: sumit
"""

import codecs, sys

data_file = codecs.open(str(sys.argv[1]), 'r', encoding = 'utf8', errors='ignore')

#data_file = codecs.open("ngram_count.py", 'r', encoding = 'utf8')

text = data_file.read()

data_file.close()

unique_tokens = sorted(set(text.split()), reverse = True)

#percentage_unique_tokens = 

unique_tokens_list = list(unique_tokens)

"""
for item in unique_tokens_list:
    print("Count of '" + str(item) + "' : " + str(text.count(str(item))) + "\n")
    print("Percentage of '" + str(item) + "' : " + str(float(100 * text.count(item) / len(text.split()))) + "%\n")
"""   

print("Total: " + str(len(text.split())))
print("Unique: " + str(len(unique_tokens)))
percentage = float(len(unique_tokens))/float(len(text.split()))
print("Percentage: " + str(percentage))