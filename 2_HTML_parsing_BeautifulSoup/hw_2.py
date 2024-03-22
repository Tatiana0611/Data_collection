import requests
from bs4 import BeautifulSoup
import json
import re

base_url = "http://books.toscrape.com/"
url = base_url + "catalogue/page-1.html"
pages_counter = 0
books = []

while url:
    print("\nПроводится скрапинг страницы №", pages_counter + 1)
    # Отправка GET запроса по URL
    response = requests.get(url)

    # Парсинг HTML страницы с использованием BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    h3_tags = soup.find_all("h3")

    for h3_tag in h3_tags:
        a_tag = h3_tag.find("a", href=True)
        book_url = base_url + "catalogue/" + a_tag["href"]
        book_response = requests.get(book_url)
        book_soup = BeautifulSoup(book_response.text, "html.parser")
        title = book_soup.find("h1").text.strip()
        price = float(book_soup.find("p", class_="price_color").text.strip().replace("Â\u00a3", ""))
        stock = int(re.findall(r'\d+', book_soup.find("p", class_="instock availability").text.strip())[0])
        description = book_soup.find("meta", attrs={"name": "description"})["content"]
        books.append({
            "Название": title,
            "Цена": price,
            "Количество": stock,
            "Описание": description
        })
        print(title)

    next_button = soup.find('a', string='next')

    if next_button:
        url = base_url + "catalogue/" + next_button['href']
        pages_counter += 1
    else:
        url = None

with open("books_from_books.toscrape.com.json", "w", encoding='utf-8') as f:
    json.dump(books, f, indent=4, ensure_ascii=False)
