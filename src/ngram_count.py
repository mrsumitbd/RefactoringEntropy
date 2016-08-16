# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:47:47 2016

@author: MusfiqurRahman
"""

import nltk, sys
from nltk.util import ngrams
from collections import Counter
import operator



def count_ngram():
    f = open(sys.argv[1], 'r') #reading
    text = f.read() #file
    f.close()   #for data
    token = nltk.word_tokenize(text)    #tokenize read data
    Ngrams = ngrams(token, int(sys.argv[2]))    #count n gram
    c =  dict(Counter(Ngrams))  #conver counter object to a dictionary so that we can sort according to the order of the value
    sorted_c = sorted(c.items(), key=operator.itemgetter(1), reverse = True) #sorted_c is a list of tuples
    write_to_file(sorted_c)

def write_to_file(sorted_data):
    FILE = open(sys.argv[3], 'w')
    for x in range (0, len(sorted_data)):
        FILE.write(str((sorted_data[x])[0]) + "\t" + str((sorted_data[x])[1]) + "\n")
    
    FILE.close()

if __name__ == "__main__":
    count_ngram()
