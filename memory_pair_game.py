import random

number_of_items = int(input("Input number of items: " )) #12, 16, 20, 24

all_names = ["apple", "peach", "banana", "kiwi", "watermelon", "strawberry", "pineapple", "blueberry"] * 3

names = all_names[:number_of_items // 2] * 2

#перемешаем names
for i in range(100):
    a = random.randint(0, number_of_items-1)
    b = random.randint(0, number_of_items-1)
    names[a], names[b] = names[b], names[a]
print(names)

#начинаем играть
inGame = [True for i in range(number_of_items)]
steps = 0
while inGame.count(True):
    print(f"Input 2 numbers from 0 to {number_of_items}: ")


    flag = True
    while flag:
        a = int(input())
        if inGame[a] == False:
            print("You have already picked it. Choose another one")
        else:
            flag = False
    print(f"{names[a]}")
    flag = True
    while flag:
        b = int(input())
        if inGame[b] == False:
            print("You have already picked it. Choose another one")
        else:
            flag = False
    print(f"{names[b]}")


    if names[a] == names[b]:
        inGame[a] = False
        inGame[b] = False
        print("Great! :)")
    else:
        print("Not a pair, try more :(")
    steps+=1
print(f"Congratulations! You won! It took {steps} steps.")
    







