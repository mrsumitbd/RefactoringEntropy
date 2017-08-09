# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:47:47 2016

@author: MusfiqurRahman
"""

import nltk, sys, codecs, csv
from nltk.util import ngrams
from collections import Counter
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
    c = Counter(Ngrams)
    write_to_file(c.most_common())


def write_to_file(sorted_data):
    data_row = []
    total = 0
    for i in range (0, len(sorted_data)):
        total = total + int((sorted_data[i])[1])
    for x in range (0, len(sorted_data)):
        print(str((sorted_data[x])[0]), str((sorted_data[x])[1]), str(((sorted_data[x])[1]*100.0)/total))
        data_row.append((sorted_data[x])[0])
        data_row.append(float((sorted_data[x])[1]))
        data_row.append(float(((sorted_data[x])[1]*100.0)/total))
        writer.writerow(data_row)
        del data_row[:]


if __name__ == "__main__":
    outputfile = open(sys.argv[3], "wb")
    writer = csv.writer(outputfile, delimiter='\t', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)

    count_ngram()
    
    outputfile.close()
