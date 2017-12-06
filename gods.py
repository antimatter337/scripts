#! /usr/bin/env python 

from bs4 import BeautifulSoup
from urllib.request import urlopen


site = "https://tiraas.wordpress.com/"

print("Currently on 13 – 26")
print(" ")

def get_soup():
    global soup
    html = urlopen(site)
    soup = BeautifulSoup(html, "lxml") 
    return soup

def get_text():
    for i in soup.body("h1", {"class": "entry-title"}):
        text = i.get_text()
        text = text.replace("\n", "")
        print(f'Newest chapter is {text}')




def final():
    get_soup()
    get_text()


final()
