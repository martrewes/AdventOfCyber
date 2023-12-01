#Grabber.py

``` python
# Import the libraries we downloaded earlier
# if you try importing without installing them, this step will fail
from bs4 import BeautifulSoup
import requests 

# replace testurl.com with the url you want to use.
# requests.get downloads the webpage and stores it as a variable
html = requests.get('http://10.10.205.219:80').text 

# this parses the webpage into something that beautifulsoup can read over
soup = BeautifulSoup(html, "lxml")
# lxml is just the parser for reading the html 
# print(soup)
# this is the line that grabs all the links # stores all the links in the links variable
links = soup.find_all("a") 
#print(links)

for link in links:      
    # prints each link 
    if "href" in link.attrs: 
        print(link["href"])
```