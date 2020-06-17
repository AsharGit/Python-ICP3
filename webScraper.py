import requests
from bs4 import BeautifulSoup

html = requests.get('https://en.wikipedia.org/wiki/Deep_learning')
soup = BeautifulSoup(html.content, 'html.parser')
file = open('links.txt', 'w')

# Print title
print(soup.title)

# Find links in url with <a> tag
soup.find_all('a')

# Find links in url with 'href' attribute
# Print to console and save to txt file
for link in soup.find_all('a'):
    print(link.get('href'))
    file.write(str(link.get('href')))
    file.write('\n')

file.close()


