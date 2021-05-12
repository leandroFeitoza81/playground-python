from parsel import Selector
import requests

URL_BASE = "http://books.toscrape.com/catalogue/"
page_url = "page-1.html"

while page_url:
    response = requests.get(URL_BASE + page_url)
    selector = Selector(text=response.text)

    for book in selector.css(".product_pod"):
        title = book.css("h3 a::attr(title)").get()
        price = book.css(".price_color::text").get()
        print(title, price)

    page_url = selector.css(".next a::attr(href)").get()
