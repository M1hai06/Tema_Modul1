#Deretei Luca-Mihai
import webbrowser
'''Deschide URL-uri in Browser'''
url = input()
webbrowser.open_new_tab(url)
from urllib.request import urlopen
'''Efectueaza cereri HTTP'''
from bs4 import BeautifulSoup
'''Extrage informatii din documente HTML,XML'''
page = urlopen(url)
link = BeautifulSoup(page, 'html.parser')
print(link.title.string)
meta_tags = link.find_all('meta')
for tag in meta_tags:
    if 'content' in tag.attrs:
        print(tag.get('content'))
