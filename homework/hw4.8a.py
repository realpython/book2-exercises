# Beautiful Soup find all links


from bs4 import BeautifulSoup
import requests

# specifices the url to scrape
url = "http://www.web2py.com"

# grabs the html source code from the url
html = requests.get(url).text

# parses the html
soup = BeautifulSoup(html)

# display each link to screen
for link in soup.findAll('a'):
    print link.get('href')

