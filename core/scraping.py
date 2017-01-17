import urllib.request
from lxml import html
from bs4 import BeautifulSoup

class Scraping():

    def count_word(url, selected_word):
        html = urllib.request.urlopen(str(url)).read().decode("utf-8")

        soup = BeautifulSoup(html, "html.parser")

        content = soup.get_text()

        words = content.split()

        word_quantity = 0

        for word in words:
            if word.lower() == selected_word.lower():
                word_quantity += 1

        return word_quantity