import bs4 as bs
import json 
import sys
import nltk #tokenizer
import string
from collections import defaultdict

#query given by user
query = ''
indexDic = defaultdict(list)
mergedList = []
loopCounter = 0

#path for windows, comment this and create new path for mac
#bookkeepingPath = '../gicsggle/Database/WEBPAGES/WEBPAGES_RAW/'
bookkeepingPath = '/Users/wang/Desktop/2018 Spring/CS 121 Information Retrieval/Homework/Assignment 3/WEBPAGES_RAW/'

#reading from bookkeeping json
with open(bookkeepingPath + 'bookkeeping.json', 'r') as f:
    bookkeeping = json.load(f)  #data is a dict with [keys = file num | value = url]

#go through bookkeeping dict as guide for tokenizing htmls
for key in bookkeeping:
    print key
    loopCounter += 1
    #traversing data  (key = key | bookkeeping[key] = value)
    #print "key: %s , value: %s" % (key, bookkeeping[key]) 
    currentPath = bookkeepingPath + key

    #open html file using key of bookkeeping (map)
    with open(currentPath, 'r') as html_file:
        soup = bs.BeautifulSoup(html_file, 'lxml')
        
    #//read words inside <li> tag in html file
        #for paragraph in soup.find_all('li'):
        #    words = paragraph.text
        #    print >> output, words.encode('utf-8')

        #read all words in html file
        words = soup.text

        #remove punctuation
        translate_table = dict((ord(char), None) for char in string.punctuation)
        words = words.translate(translate_table).lower()

        #tokenization
        tokens = [t for t in words.split()]

        #push into indexDic
        for t in tokens:
        	#indexDic  KEY = signal token | VALUE = key in bookkeeping(ex:13/481)
            if key not in indexDic[t]:
                indexDic[t].append(key)

        if loopCounter == 200:
        	break
    html_file.close()
f.close()

tokenNumber = len(indexDic.keys())

print ('a. Number of documents of the corpus: ' + str(loopCounter))
print ('b. Number of [unique] tokens present in the index: ' + str(tokenNumber))
print ('c. The total size (in KB) of index on disk: ' + 'manually check')



#create an output file: dictionary.json
#dictionary.json will be the dictionary we search from
with open('dictionary.json', 'w+') as output:
    json.dump(indexDic, output, indent=4, sort_keys=True)
    output.close()



#------old code------
#sorting dictionary
#for a in sorted(indexDic):
    #print >> output, (a,':',indexDic[a])
    #index = "%s , %s" % (a, indexDic[a])
    #print >> output, (index.encode('utf-8'))





