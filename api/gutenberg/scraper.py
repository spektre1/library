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


def parseBookInfo(bookID:int):
    """Get Bibliographic record data about a book."""
    bookID = str(bookID) if isinstance(bookID, int) else bookID
    URLBookPrefix = 'https://www.gutenberg.org/ebooks/'
    resp = requests.get(URLBookPrefix + bookID)
    soup = BSoup(resp.content, 'lxml-xml')

    bookMeta = {}
    bookMeta['coverImgURL'] = soup.find(id="cover").img['src']
    bookMeta['textURL'] = soup.find(id='download').find(
        string=re.compile("Plain Text")).parent['href']

    # Get biblographic record:
    trs = soup.find(id="bibrec").table.find_all('tr')
    for tr in trs:
        if tr.td and tr.th:
            # This is a generalized way to append multiple Subjects onto a
            # list in the returned dict
            value = tr.td.get_text().strip()
            key = tr.th.get_text()
            if key in bookMeta:
                if isinstance(bookMeta[key], list):
                    bookMeta[key].append(value)
                else:
                    bookMeta[key] = [bookMeta[key], value]
            else:
                bookMeta[key] = value
    return bookMeta

