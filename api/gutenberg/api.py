"""Scrape the list of top 100 eBooks Last 30 Days, get the Title/Author of them,
download a copy.

BookID is the 
"""
from bs4 import BeautifulSoup as BSoup
from bs4 import Tag, NavigableString
import requests
import re


def assignToDictAsList(dictionary, key, value):
    """If we try to assign a value to a key in a dict that already exists,
    instead turn that value into a list if it isn't yet, then append the value
    to the list.
    !: this is somewhat side effect heavy as not returning the dict,
    modifying a mutable which ugh."""
    if key in dictionary:
        if isinstance(dictionary[key], list):
            dictionary[key].append(value)
        else:
            dictionary[key] = [dictionary[key], value]
    else:
        dictionary[key] = value

class Gutenberg():
    baseURL = 'https://www.gutenberg.org/'

    def get(self, url):
        """Abstracting this to do sessions. TODO: add session logic from ameliaPy."""
        return requests.get(self.baseURL + url)

    def getTopTitles(self) -> list[tuple[str, str, str, str]]:
        """Reads URLTopList and gets last 30 days top 100 titles.
        Returns list of tuples of Title, Author, DownloadCount, ID.
        Known issue: Regex fails on titles in the list that don't list an
        author, i.e. Beowulf."""
        resp = self.get('browse/scores/top#books-last30')
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

    def getBookInfo(self, bookID:int):
        """Get Bibliographic record data about a book."""
        bookID = str(bookID) if isinstance(bookID, int) else bookID
        resp = self.get('ebooks/' + bookID)
        soup = BSoup(resp.content, 'lxml-xml')

        bookMeta = {
            'coverImgURL': soup.find(id="cover").img['src'],
            'textURL': soup.find(id='download').find(
                string=re.compile("Plain Text")).parent['href']
        }

        # Get biblographic record:
        for tr in soup.find(id="bibrec").table.find_all('tr'):
            if tr.td and tr.th:
                assignToDictAsList(bookMeta,
                    tr.th.get_text(),
                    tr.td.get_text().strip())
        return bookMeta
