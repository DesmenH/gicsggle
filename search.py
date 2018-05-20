import json
from collections import OrderedDict #used to import orderedDict

#input: json file with dictionary
#output: dictionary of searchMap
def loadDict(inputDictPath):
    with open(inputDictPath, 'r') as dict:
        searchMap = json.load(dict, object_pairs_hook = OrderedDict)
        dict.close()
        return searchMap

def searchDict(term, dict, addressMap, kvalue):
    if term in dict:
        addressList = dict[term]  #addressList is a list of all address from bookkeeping

        #open bookkeeping to search for url
        with open(addressMap, 'r') as bookkeeping_file:
            addressDict = json.load(bookkeeping_file, object_pairs_hook = OrderedDict)
            bookkeeping_file.close()
        
        #traverse list of paths found -> inside bookkeeping.json
        print ("%s results found") % len(addressList)
        print ("%s results shown \n") % kvalue
        
        counter = 0
        for address in addressList:
            print (addressDict[address])
            print (" ")
            counter += 1
            if counter == kvalue:
                break
    else:
        printUnfound()
     
def printUnfound():
        print "Your search - %s - did not match any documents." % term
        print "\n Suggestions: \n"
        print "  - Make sure all words are spelled correctly."
        print "  - Try different keywords."
        print "  - Try more general keywords."
        print "  - Try fewer keywords."


