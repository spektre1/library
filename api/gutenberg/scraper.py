"""This scrapes the top 100 books of the last 30 days, and writes a json
file with their biblographic record."""
from gutenberg.api import Gutenberg
import json

G = Gutenberg()

titles = G.getTopTitles()

# Wittgenstein doesn't have a plaintext file:
# G.getBookInfo(titles[71][3])

bookInfo = []
for title in titles:
    bookInfo.append(G.getBookInfo(title[3]))

# make all authors lists, API expects this
for book in bookInfo:
    if isinstance(book['author'], str):
        book['author'] = [book['author']]

# Write bookInfo to file:
with open('gutenberg100.json', 'w') as f:
    f.write(json.dumps(bookInfo, sort_keys=True, indent=2))
