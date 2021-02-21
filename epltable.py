#! python3

import requests 
from bs4 import BeautifulSoup
import pandas as pd

# Load the webpage content
r = requests.get('https://www.premierleague.com/tables') 

# Convert to beautiful soup object
soup = BeautifulSoup(r.content, features='lxml')

# removing all the extra tags at once - then passing the soup object directly to pandas
class_names = [ 'revealMore', 'short', 'thShort', 'linkable', 'expandable', 'movement' ]

for tag in soup.find_all(class_=class_names):
    tag.decompose()

df = (pd.read_html(str(soup))[0]) 
print(df)

