import httplib2
from bs4 import BeautifulSoup, SoupStrainer
from sys import exit
import time 

# importing httplib2 to handle urls and requests
# and importing BeautifulSoup to scrape the returned html page and parse the urls
# sys library to control the script
# to handle sleeping time


def get_urls(url):

#this function gets a url 
#open that url 
#and get all urls in that page 
#and correct the incomplete urls


    nested_urls=list()             
    #list to save all the urls

    http = httplib2.Http()
    status, response = http.request(url)

    #sleep time to avoid locking my ip from wikipedia server if i send so many requests in small time
    time.sleep(0.5)
    
    # for loop that will itterate on all urls to get the urls
    for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):

        if link.has_attr('href'):

            if "wiki" in link["href"]:
            #as the page can has some urls tat for other sites than wikipedia we wont save them

                if "https" not in link["href"]:
                #we search for incomplete urls to correct them 
                    link["href"]="https://en.wikipedia.org"+link["href"]
                    nested_urls.append(link["href"])
    return nested_urls



# beginning of the programm asking the user for the starting and goal urls 
start=input("enter starting link : ")
end=input("enter target link : ")


# checking if the start is the goal
if start==end:
    print("the starting url is the one you want to search for")
    exit(0)

# if not i send the starting url for scrapping and parsing 
urls = get_urls(start)

# i will use queue data stracture idea to search for the link like BFS searching algorithm
queue=list()

for i in urls:
    queue.append(i)

# i will save visited urls in a list 
# fistly to avoid loops
# secondly to print after finding the goal
visited_urls=list()


while 1 :
    # getting the first element to search 
    current_url=queue.pop(0)

    # condition to avoid loops 
    if current_url in visited_urls :
        continue

    # if its not the goal open the url to get all urls in it
    if current_url != end:
        visited_urls.append(current_url)
        urls2=get_urls(current_url)
        for i in urls2:
            queue.append(i)

    # if its the goal print visited urls then break the loop
    if current_url == end:
        print("the visited urls to the end is :")
        for i in visited_urls:
            print(i)
        exit(0)
