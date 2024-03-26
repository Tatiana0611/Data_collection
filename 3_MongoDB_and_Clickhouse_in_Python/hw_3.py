from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['hw']
books_info = db.books_info

with open('books.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

for book in books:
    books_info.insert_one(book)

for doc in books_info.find({'Название': 'A Light in the Attic'}):
    print(doc)

for doc in books_info.find({"Цена": {"$gt": 50}}, {"_id": 0, "Описание": 0}):
    print(doc)

for doc in books_info.find({"$or": [{"Цена": {'$lt': 20}}, {"Количество": {"$gt": 50}}]}, {"_id": 0, "Описание": 0}):
    print(doc)

new_data = {
        "Название": "Maths",
        "Цена": 5,
        "Количество": 80,
        "Описание": "\nIn addition to students, this book will appeal to readers of apologetics. ...more\n"
}

books_info.update_one({'Название': 'A Light in the Attic'}, {'$set': new_data})

for doc in books_info.find({'Название': 'Maths'}):
    print(doc)

books_info.delete_many({'Название': 'A Light in the Attic'})

for doc in books_info.find({'Название': 'A Light in the Attic'}):
    print(doc)