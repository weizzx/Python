import random

def GenPass():
    array = []
    password = ""
    index = 1
    Numbers = "1234567890"
    lLetters = "abcdefghijklmnopqrstuvwxyz"
    uLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Symbols = '.,/?!@#$%^&*'
    lenght = 16 #int(input())
    lenght /= 4

    while index <= lenght:
        rand = random.choice(Numbers)
        array.append(rand)
        rand = random.choice(lLetters)
        array.append(rand)
        rand = random.choice(uLetters)
        array.append(rand)
        rand = random.choice(Symbols)
        array.append(rand)

        index+=1

    for x in array:
        password += x
    
    return password
