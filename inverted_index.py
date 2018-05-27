import bs4 as bs
import json 
import sys
import nltk #tokenizer
import string
from collections import defaultdict
import os #used to store in PostingList Folder
import math #used for tf-idf
import search

#query given by user
query = ''
indexDic = defaultdict(list)
mergedList = []
loopCounter = 0

#path for windows, comment this and create new path for mac
bookkeepingPath = '../gicsggle/Database/WEBPAGES/WEBPAGES_RAW/'
#bookkeepingPath = '/Users/wang/Desktop/2018 Spring/CS 121 Information Retrieval/Homework/Assignment 3/WEBPAGES_RAW/'

#path for posting list
plPath = '../gicsggle/PostingList'

#loading searchMap
searchMap = search.loadDict("bookkeeping.json")

#reading from bookkeeping json
with open(bookkeepingPath + 'bookkeeping.json', 'r') as f:
    bookkeeping = json.load(f)  #data is a dict with [keys = file num | value = url]
    f.close()

#go through bookkeeping dict as guide for tokenizing htmls
for key in bookkeeping:
    print key
    loopCounter += 1
    #traversing data  (key = key | bookkeeping[key] = value)
    #print "key: %s , value: %s" % (key, bookkeeping[key]) 
    currentPath = bookkeepingPath + key
    url = searchMap[key]

    #open html file using key of bookkeeping (map)
    with open(currentPath, 'r') as html_file:
        soup = bs.BeautifulSoup(html_file, 'lxml')

        #read all words in html file
        words = soup.text

        #remove punctuation
        translate_table = dict((ord(char), None) for char in string.punctuation)
        words = words.translate(translate_table).lower() #lowercase

        #remove non-ascii characters
        words = "".join(nonascii for nonascii in words if ord(nonascii)<128)

        #tokenization
        tokens = [t for t in words.split()]

        #remove tokens with too many characters
        #longest word in english dictionary is 45 characters
        tokens = [longword for longword in tokens if len(longword) <= 45]
        
        #push into indexDic
        for t in tokens:
       	    #indexDic  KEY = signal token(path to data) | VALUE = key in bookkeeping(ex:13/481) -> term freq
            if len([keytfpair for keytfpair in indexDic[t] if keytfpair[0] == url]) == 0:
                #counting number of times each term occurs in document
                tf = tokens.count(t)

                #calculate weight tf-score 
                #tf-score = 1+log10(tf of term for a particular document)
                tf = 1 + math.log10(tf)

                #create a dict of key->term freq
                keywithtf = (url, tf)
                indexDic[t].append(keywithtf)

        if loopCounter == 1:
        	break
        html_file.close()

tokenNumber = len(indexDic.keys())

#report
print ('a. Number of documents of the corpus: ' + str(loopCounter))
print ('b. Number of [unique] tokens present in the index: ' + str(tokenNumber))
print ('c. The total size (in KB) of index on disk: ' + 'manually check')

outputCount = 0
foldernumber = 0
plDirectory = {}

if not os.path.exists('../gicsggle/PostingList'):
    os.makedirs('../gicsggle/PostingList')

for term in indexDic:
    #status bar
    if outputCount%250 == 0:
        print "working on file %s/%d" % (outputCount, tokenNumber)

    #create a new file for every 500 term
    if outputCount % 500 == 0:
        foldernumber += 1
        path = '/%s' % foldernumber
        path = plPath + path

    #make a new folder if it doesn't exist already
    if not os.path.exists(path):
        os.makedirs(path)

    filename = str(outputCount) + '.json'
    with open(os.path.join(path, filename), 'w+') as output:
        json.dump(indexDic[term], output, indent=4)
        output.close()

    plDirectory[term] = path
    outputCount += 1

#create a posting list bookkeeping json that will be used for searching
with open('plBookkeeping.json', 'w+') as output:
    json.dump(plDirectory, output, indent=4, sort_keys=True)
    output.close()



#create an output file: dictionary.json
#dictionary.json will be the dictionary we search from
with open('dictionary.json', 'w+') as output:
    json.dump(indexDic, output, indent=4, sort_keys=True)
    output.close()

#creating a dictionary of term->idf weight
#idf weight = log10(# of document in corpus / # of time the term showed up)
idfDic = {}
for term in indexDic:
    #print "%s : %d" % (term, len(indexDic[term]))
    idf = math.log10(loopCounter / len(indexDic[term]))
    idfDic[term] = idf

#output the idfDic as a json
with open('idf.json', 'w+') as output:
    json.dump(idfDic, output, indent=4, sort_keys=True)
    output.close()


#------old code------
#sorting dictionary
#for a in sorted(indexDic):
    #print >> output, (a,':',indexDic[a])
    #index = "%s , %s" % (a, indexDic[a])
    #print >> output, (index.encode('utf-8'))

#//read words inside <li> tag in html file
    #for paragraph in soup.find_all('li'):
    #    words = paragraph.text
    #    print >> output, words.encode('utf-8')





