
# Import modules
import requests # to request website data
from bs4 import BeautifulSoup # to parse HTML and find content
from dictionary import dictionary

URL = 'https://www.glassdoor.com/Reviews/State-of-Utah-Reviews-E220438_P2.htm'
page = requests.get(URL)
print(page)

