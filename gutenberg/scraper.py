"""Scrape the list of top 100 eBooks Last 30 Days, get the Title/Author of them,
download a copy.

BookID is the 
"""
from bs4 import BeautifulSoup as BSoup
from bs4 import Tag, NavigableString
import requests
import re


def getTopTitles():
    """Reads URLTopList and gets last 30 days top 100 titles.
        Known issue: Regex fails on titles in the list that don't list an
        author, i.e. Beowulf"""
    URLTopList = 'https://www.gutenberg.org/browse/scores/top#books-last30'
    resp = requests.get(URLTopList)
    soup = BSoup(resp.content, 'lxml-xml')

    ol = soup.find(id="books-last30").find_next_sibling("ol")

    BookData = re.compile(r'(.+) by (.+) \(([\d]+)\)')
    topTitles = []
    for i in ol.children:
        if isinstance(i, NavigableString):
            continue
        if isinstance(i, Tag):
            text = i.a.contents[0]
            bookID = i.a['href'].lstrip('/ebooks/')
            match = BookData.search(text)
            if match:
                data = match.groups()
                topTitles.append((*data, bookID)) # This is recomposing a tuple
    return topTitles


def parseBookInfo():
    """Get Bibliographic record data about a book."""
    URLBookPrefix = 'https://www.gutenberg.org/ebooks/'
    bookID = 140 # Upton Sinclair, the Jungle
    resp = requests.get(URLBookPrefix + str(bookID))
    soup = BSoup(resp.content, 'lxml-xml')

    d = soup.find(id="bibrec")

    trs = d.table.find_all('tr')

    kv = {}
    kv['Subject'] = []
    for tr in trs:
        if tr.td and tr.th:
            # This is a generalized way to append multiple Subjects onto a
            # list in the returned dict
            value = tr.td.get_text().strip()
            key = tr.th.get_text()
            if key in kv:
                if isinstance(kv[key], list):
                    kv[key].append(value)
                else:
                    kv[key] = [kv[key], value]
            else:
                kv[key] = value
    return kv

