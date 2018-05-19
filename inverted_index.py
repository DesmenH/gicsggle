import bs4 as bs
import json 
import sys


#path for windows, comment this and create new path for mac
bookkeepingPath = '../giscggle/Database/WEBPAGES/WEBPAGES_RAW/' 

#reading from bookkeeping json
with open(bookkeepingPath+'bookkeeping.json', 'r') as f:
    bookkeeping = json.load(f)  #data is a dict with [keys = file num | value = url]

#go through bookkeeping dict as guide for tokenizing htmls
for key in bookkeeping:

    #traversing data  (key = key | bookkeeping[key] = value)
    #print "key: %s , value: %s" % (key, bookkeeping[key]) 
    currentPath = bookkeepingPath + key

    #open html file using key of bookkeeping (map)
    with open(currentPath, 'r') as html_file:
        soup = bs.BeautifulSoup(html_file, 'lxml')
        
        #create an output file: test.txt
        #test.txt will have all text inside in html file
        with open('test.txt', 'w+') as output:

            #//read words inside <li> tag in html file
            #for paragraph in soup.find_all('li'):
            #    words = paragraph.text
            #    print >> output, words.encode('utf-8')

            #read all words in html file
            words = soup.text
            print >> output, words.encode('utf-8')
            output.close()        

        print currentPath
        exit()
        html_file.close()

f.close()






