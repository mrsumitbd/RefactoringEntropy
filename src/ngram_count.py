# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:47:47 2016

@author: MusfiqurRahman
"""

import nltk, sys, codecs, csv
from nltk.util import ngrams
reload(sys)  
sys.setdefaultencoding('utf8')

"""
Example command:

python ngram_count.py /path/to/input/file valueofN /path/to/output/file
"""



def count_ngram():
    f = codecs.open(sys.argv[1], 'r', encoding='utf8', errors='ignore') #reading
    text = f.read() #file
    f.close()   #for data
    token = nltk.word_tokenize(text)    #tokenize read data
    Ngrams = ngrams(token, int(sys.argv[2]))    #count n gram
    ngram_list = []
    for ngram in Ngrams:
        ngram_list.append(ngram)
    print(len(ngram_list))
    fdist = nltk.FreqDist(ngram_list)
    write_to_file(fdist)


def write_to_file(freqDist):
    total = 0
    for count in freqDist.items():
        total += int(count[1])
    
    data_row = []

    for k, v in freqDist.items():
        print("Writing " + str(k) + "...")
        data_row.append(k)
        data_row.append(float(v))
        data_row.append(float((v*100.0)/total))
        writer.writerow(data_row)
        del data_row[:]


if __name__ == "__main__":
    outputfile = open(sys.argv[3], "wb")
    writer = csv.writer(outputfile, delimiter='\t', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)

    count_ngram()
    
    outputfile.close()
