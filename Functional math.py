x = 1
import pandas as More_pandas
import random
def ran():
    for i in range(1):
        yield random.randint(10, 100)
def rand():
    for i in range(1):
        yield random.randint(10, 50)
def name():
    Name = input("What is your name?: ")
    return Name
while (x < 6):
    for random_number in ran():
        def number1():
            a = random_number
            return a
    for random_number in rand():
        def number2():
            b = random_number
            return b
    def question():
        a = number1
        b = number2
        return "Solve the following equation. %d * %d?:" % a, b
    def answer():
        a = number1
        b = number2
        c = a + b
        return c
    def ask():
        q = question()
        pa = int(input((q)))
    ask()
    
