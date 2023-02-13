"""Scrape the list of top 100 eBooks Last 30 Days, get the Title/Author of them,
download a copy.
"""
from bs4 import BeautifulSoup as BSoup
from bs4 import Tag, NavigableString
import requests
import re


parse = re.compile(r'([\w\s]+) by ([\w\s]*) \(([\d]+)\)')

URLTopList = 'https://www.gutenberg.org/browse/scores/top#books-last30'



resp = requests.get(URLTopList)
soup = BSoup(resp.content, 'lxml-xml')


ol = soup.find(id="books-last30").find_next_sibling("ol")

for i in ol.children:
    if isinstance(i, NavigableString):
        continue
    if isinstance(i, Tag):
        text = i.a.contents[0]
        title, author, downloadCount = parse.search(text).groups()

