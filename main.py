import requests
from bs4 import BeautifulSoup
from db import store


def get_html(url):
    res = requests.get(url)
    return res.text


def select(data: object):
    soup = BeautifulSoup(data, 'html.parser')
    res: list = soup.find_all("article")
    titles: list = [i.find("img")["alt"] for i in res]
    stock: list = [i.find(class_="instock availability").get_text().replace(
        "\n", "") for i in res]
    price: list = [i.find(class_="price_color").get_text() for i in res]
    return list(zip(titles, stock, price))


def main():
    html = get_html(
        "http://books.toscrape.com/")
    res = select(html)
    store(res)
    print("Done")


if __name__ == "__main__":
    main()
