from gutenberg.api import Gutenberg

G = Gutenberg()

titles = G.getTopTitles()
# book = G.getBookInfo(titles[0][3])

bookInfo = []
for title in titles:
    bookInfo.append(G.getBookInfo(title[3]))
