with open("book.txt", "r") as f:
    book = f.read()

print(book)
print(type(book))

import json
book = json.loads(book)

print(book)
print(type(book))

print(book["islam"]["address"])