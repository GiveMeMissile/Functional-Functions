x = 1
import pandas as More_pandas
import random
Name = input("What is your name?: ")
def ran():
    for i in range(1):
        yield random.randint(10, 100)
def rand():
    for i in range(1):
        yield random.randint(1, 50)
def name():
    Name = input("What is your name?: ")
    return Name
while (x < 6):
    for random_number in ran():
        a = random_number
    for random_number in rand():
        b = random_number
    def question():
        return "Solve the following equation. %s * %s?:" % (a, b)
    def answer():
        c = a * b
        return c
    def ask():
        q = question()
        pa = int(input((q)))
        return pa
    def corrin():
        pa = ask()
        c = answer()
        if(pa == c):
            print("Correct")
            return "Correct"
        else:
            print("Incorrect, The answer was %d" % (c))
            return "Incorrect"
    corrin()
    def collection():
