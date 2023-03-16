import scrapy
from bs4 import BeautifulSoup
from ..items import AmazonscrapeItem


class BooksSpider(scrapy.Spider):
    name = 'new_books'
    start_urls = [
        "https://www.amazon.com/gp/bestsellers/2009/books",
        "https://www.amazon.com/gp/bestsellers/2010/books/"
    ]

    # start_urls = urls

    def parse(self, response):
        items = AmazonscrapeItem()
        soup = BeautifulSoup(response.text, 'html.parser')
        books_soup = soup.find_all(id='gridItemRoot')

        # books = response.css('div#gridItemRoot')

        for book in books_soup:
            price0 = book.find('span', class_="_cDEzb_p13n-sc-price_3mJ9Z")
            price = price0.text[1:] if price0 else None
            rank0 = book.find('span', class_='zg-bdg-text')
            rank = rank0.text[1:] if rank0 else None
            title0 = book.find('div', class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y")
            title = title0.text if title0 else None
            no_of_reviews0 = book.find('span', class_="a-size-small")
            no_of_reviews = no_of_reviews0.text if no_of_reviews0 else None
            cover_type0 = book.find('span', class_="a-size-small a-color-secondary a-text-normal")
            cover_type = cover_type0.text if cover_type0 else None
            author0 = book.find('a', class_="a-size-small a-link-child")
            author = author0.text if author0 else None
            ratings0 = book.find('span', class_="a-icon-alt")
            ratings = ratings0.text[:3] if ratings0 else None
            years = response.css('h1.a-size-large::text').get()[-4:]
            year = int(years)

            items['price'] = price
            items['rank'] = rank
            items['title'] = title
            items['no_of_reviews'] = no_of_reviews
            items['author'] = author
            items['ratings'] = ratings
            items['year'] = year
            items['cover_type'] = cover_type

            yield items
