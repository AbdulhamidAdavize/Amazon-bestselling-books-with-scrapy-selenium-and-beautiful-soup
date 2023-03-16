import scrapy
from bs4 import BeautifulSoup
from ..items import AmazonscrapeItem

urls = []
years = [str(i) for i in range(2009, 2022)]
for year in years:
    urls.append(f"https://www.amazon.com/gp/bestsellers/{year}/books")
    urls.append(f"https://www.amazon.com/gp/bestsellers/{year}/books/ref=zg_bsar_pg_2/ref=zg_bsar_pg_2?ie=UTF8&pg=2")



class BooksSpider(scrapy.Spider):

    name = 'books'
    start_urls = [
    "https://www.amazon.com/gp/bestsellers/2009/books",
    "https://www.amazon.com/gp/bestsellers/2009/books/ref=zg_bsar_pg_2/ref=zg_bsar_pg_2?ie=UTF8&pg=2"
    ]

    # start_urls = urls

    def parse(self, response):
        items = AmazonscrapeItem()
        #soup = BeautifulSoup(response.text, 'html.parser')
        #books_soup = soup.find_all(id='gridItemRoot')

        books = response.css('div#gridItemRoot')

        for book in books:
            #soup = BeautifulSoup(book.body, 'lxml')

            yield{
                'year': response.css('h1.a-size-large::text').get()[-4:],
                'rank': book.css('span.zg-bdg-text::text').get()[1:],
                'title': book.css('a.a-link-normal').xpath('.//div/text()').get(),
                'author': book.css('a.a-link-child').xpath('.//div/text()').get(),
                'ratings':  book.css('span.a-icon-alt::text').get()[:3],
                'cover_type': book.css('span.a-text-normal::text').get(),
                'no_of_reviews': response.css('a.a-link-normal').css('span.a-size-small::text').get()
            }

