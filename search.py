import json
from collections import OrderedDict #used to import orderedDict

#input: json file with dictionary
#output: dictionary of searchMap
def loadDict(inputDictPath):
    with open(inputDictPath, 'r') as dict:
        searchMap = json.load(dict, object_pairs_hook = OrderedDict)
        dict.close()
        return searchMap

#input: term and dictionary to search term in
#output: found: value of term in dict if found
#    not found: Your search - %s - did not match any documents...
def searchDict(term, dict):
    if term in dict:
        print dict[term]
    else:
        print "Your search - %s - did not match any documents." % term
        print "\n Suggestions: \n"
        print "  - Make sure all words are spelled correctly."
        print "  - Try different keywords."
        print "  - Try more general keywords."
        print "  - Try fewer keywords."
    
    

