# making a dictionary
book = {}
book['islam'] = {
    'name': 'Islam',
    'address': 'Pakistan',
    'phone':11223344
}

book['Owais'] = {
    'name': 'Owais',
    'address': 'India',
    'phone': 99887766
}

import json

book = json.dumps(book)
print(type(book))

with open('book.txt',"w") as f:
    f.write(book)