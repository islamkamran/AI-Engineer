dict_populaiton = {
    "USA": 32,
    "India": 136,
    "China": 143,
    "Pakistan": 21
}

while(True):
    prompt = input("Enter your prompt: ")
    if prompt.lower() == "print":
        for key in dict_populaiton:
            print(f'{key} ===> {dict_populaiton[key]}')
        
    elif prompt.lower() == "add":
        country = input("Enter Country Name: ")
        if country in dict_populaiton:
            print("This Country is already Existing")
        else:
            population = input("Enter population of the country: ")
            dict_populaiton[country] = population
        
            print(dict_populaiton)
        
    elif prompt.lower() == "remove":
        country = input("Enter Country Name: ")
        if country in dict_populaiton:
            del dict_populaiton[country]
        else:
            print("This Country is doesn't Exist")
        
    elif prompt.lower() == "query":
        country = input("Enter Country Name: ")
        if country in dict_populaiton:
            print(f'{country} ===> {dict_populaiton[country]}')
        else:
            print("This Country is doesn't Exist")
    elif prompt.lower() == "exit":
        break

    else:
        print("Invalid Prompt")     