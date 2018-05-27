import search
import sys #used for input

#main function
def main():
    #load from database
    searchMap = search.loadDict("dictionary.json")

    #prompt user for input
    searchInput = raw_input("Gicsggle Search: ")
    searchInput = searchInput.lower()

    #for printing searchMap
    #for a in searchMap:
    #    print "%s , %s" % (a, searchMap[a])

    #search for term
    search.searchDict(searchInput, searchMap, "bookkeeping.json", 20)

#main check
if __name__ == "__main__":
   main()




