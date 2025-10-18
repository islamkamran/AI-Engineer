d = {"islam":1234, "Hamdan":5678}
print(d["islam"])

d["Muhammad"] = 443322
print(d)

for key in d:
    print(f'"Key":{key} has "Value":{d[key]}')

print("---------- Print by Tuple ---------")
for k,v in d.items():
    print(f'key: {k}, Value:{v}')

# checking the python condition true or false
print("islam" in d)


d.clear()
print(d)

point = (23,72)
x = point[0]
print(x)
# checking error condtion run time assignment
# point[0]=44
# print(x)
point=(44,72)
x = point[0]
print(x)

import math

print(math.sqrt(16))

print(dir(math))