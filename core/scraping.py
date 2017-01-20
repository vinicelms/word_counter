from urllib import request, parse
from lxml import html
from bs4 import BeautifulSoup

class Scraping():

    def count_word(url, selected_word):
        p = parse.urlparse(url)
        if not p.scheme or not p.netloc:
            raise ValueError("URL is not valid!")

        html = request.urlopen(str(url)).read().decode("utf-8")

        soup = BeautifulSoup(html, "html.parser")
        for script in soup(["script", "style"]):
            script.extract()

        content = soup.get_text()

        words = content.split()

        word_quantity = 0

        for word in words:
            if word.lower() == selected_word.lower():
                word_quantity += 1

        return word_quantity