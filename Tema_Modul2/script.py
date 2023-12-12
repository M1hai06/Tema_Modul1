#Deretei Luca-Mihai
import webbrowser
'''Deschide URL-uri in Browser'''
import configparser
'''Utilizat pentru manipularea cheilor si valorilor din fisierul de configuratie ini'''
config_file = 'config.ini'
config = configparser.ConfigParser()
config.read(config_file)
url=config.get('Spec', 'url', fallback='')
if url:
        print("URL-ul citit din configurare: ",url)
else:
        print("URL-ul nu a fost specificat în configurare.")
        exit()
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


