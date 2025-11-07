# Lets say you are running a 5 km race. Write a program that:
completion = 0

for i in range(5):
    print("are You Tired?")
    answer = input('Enter Your Answer: ')
    if answer.lower() == 'yes':
        print("You did't finish the race")
        break
    completion = completion+1
    print(f"{completion}km Completed - Continue Racing you are doing great!!!")

if completion == 5:
    print("Congratulation you did it")
    

# *
# **
# ***
# ****
# *****

for i in range(1,6):
    for k in range(i):
        print("*",end="")
    print() 