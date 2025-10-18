d = {"islam":1234, "Hamdan":5678}
print(d["islam"])

d["Muhammad"] = 443322
print(d)

for key in d:
    print(f'"Key":{key} has "Value":{d[key]}')

print("---------- Print by Tuple ---------")
for k,v in d.items():
    print(f'key: {k}, Value:{v}')