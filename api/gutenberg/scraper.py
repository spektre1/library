"""This scrapes the top 100 books of the last 30 days, and writes a json
file with their biblographic record."""
from gutenberg.api import Gutenberg
import json

G = Gutenberg()

titles = G.getTopTitles()

bookInfo = []
for title in titles:
    bookInfo.append(G.getBookInfo(title[3]))

# Write bookInfo to file:
with open('gutenberg100.json', 'w') as f:
    f.write(json.dumps(bookInfo, sort_keys=True, indent=2))
