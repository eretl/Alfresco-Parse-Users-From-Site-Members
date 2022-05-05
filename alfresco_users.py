from encodings import utf_8
from bs4 import BeautifulSoup

#https://share.example.com/share/page/site/XXXX/site-members
alfresco_html = open("alfresco.html", encoding="utf_8").read()
bs = BeautifulSoup(alfresco_html, features="html.parser")

divTag = bs.find_all("div", {"class": "finder-wrapper"})
for tag in divTag:
    aTags = tag.find_all("a")
    for tag in aTags:
        print(tag.text, end = " ")