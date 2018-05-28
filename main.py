import search
import sys #used for input

#main function
def main():
    #load from database
    searchMap = search.loadDict("plBookkeeping.json")

    #prompt user for input
    searchInput = raw_input("Gicsggle Search: ")
    searchInput = searchInput.lower()

    #for printing searchMap
    #for a in searchMap:
    #    print "%s , %s" % (a, searchMap[a])

    #search for term
    postingListPath = '../gicsggle/PostingList'
    search.searchDict(searchInput, searchMap, postingListPath, 10)

#main check
if __name__ == "__main__":
   main()




