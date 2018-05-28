import json
import os
from collections import OrderedDict #used to import orderedDict

#input: json file with dictionary
#output: dictionary of searchMap
def loadDict(inputDictPath):
    with open(inputDictPath, 'r') as dict:
        searchMap = json.load(dict, object_pairs_hook = OrderedDict)
        dict.close()
        return searchMap

def searchDict(term, dict, pathToPostingList, kvalue):
    if term in dict:
        addressLoc = dict[term]  #addressLoc is a list of all address from bookkeeping
        path = os.path.join(pathToPostingList, addressLoc)

        #open file in PostingList folder containing term info
        with open(path, 'r') as bookkeeping_file:
            termDict = json.load(bookkeeping_file, object_pairs_hook = OrderedDict)
            bookkeeping_file.close()
        
        #traverse list of paths found -> inside bookkeeping.json
        print ("%s results found") % len(termDict[term])
        print ("%s results shown \n") % kvalue
        
        counter = 0
        for i in termDict[term]:
            print (i[0])
            print (" ")
            counter += 1
            if counter == kvalue:
                break
    else:
        print "Your search - %s - did not match any documents." % term
        print "\n Suggestions: \n"
        print "  - Make sure all words are spelled correctly."
        print "  - Try different keywords."
        print "  - Try more general keywords."
        print "  - Try fewer keywords."