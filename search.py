import json

#input: json file with dictionary
#output: dictionary of searchMap
def loadDict(inputDictPath):
    with open(inputDictPath, 'r') as dict:
        searchMap = json.load(dict)
        print "searchMap is a data type of: %s " % (type(searchMap))
        dict.close()
        return searchMap

#def searchDict(term, dict):


searchMap = loadDict('dictionary.json')
    
    

