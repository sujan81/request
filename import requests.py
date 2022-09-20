import requests
from bs4 import BeautifulSoup
url="https://www.onlinekhabar.com/"

# step1
r=requests.get(url)
htmlcontent=(r.content)
print(htmlcontent)

soup=BeautifulSoup(htmlcontent, 'html.parser')
print(soup.prettify())

title=soup.title
print(title)
print((typetitle))

print(type(title.string))

paragraph=soup.find('p')
print(paragraph)
print()
print(soup.find('p')

print (r)
print(r.url))
