expenses = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compared to Jan?
extra_expenses = expenses[1]-expenses[0]
print(extra_expenses)

# first quarter sum
summ = 0
for i in range(3):
    summ = summ + expenses[i]

print(summ)

# find exactly 2000 usd

for i in expenses:
    if i == 2000:
        print("yes")
        break

expenses.append(1980)

print(expenses)

expenses[4] = expenses[4]+200

print(expenses)


heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('black panther')

print(heros)

heros.remove('black panther')

heros.insert(3,'black panther')
heros[1:3]=['doctor strange']
print(heros)

print(heros.sort(reverse=False))