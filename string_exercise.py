# Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line

street = "Bur Dubai"
city = "Dubai"
country = "UAE"

address = street +"\n"+ city +"\n"+ country

print(address)

address = f'{street} \n{city} \n{country}'

print(address)


# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index

statement = "Earth revolves around the sun"
print(statement[6:14])
print(statement[-3:])


# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
s='maine 200 banana khaye'
s = s.replace('banana','samosa').replace('200','10')

print(s)