from bs4 import BeautifulSoup
import requests
import html as HTML
import random

url = 'https://www.google.com/search?q=yuzu+figure+skater+websites&tbm=isch&sa=X'
r = requests.get(url)

html = r.text

print( dir(r.raw._original_response))
raw_meat = r.raw._original_response
print("raw = " + str(raw_meat))
print(html)

soup = BeautifulSoup(html, 'html.parser') 
links = soup.find_all('a')
items = [i.get('href') for i in soup.find_all('a')]
print(items)
pick =random.choice(range(1,  len(links)))
imageUrl= HTML.unescape(links[pick].get('src'))
