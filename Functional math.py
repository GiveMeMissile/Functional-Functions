import random
import pandas as pd
def rand():
    for i in range(1):
        yield random.randint(10, 50)
def ran():
    for i in range(1):
        yield random.randint(4, 20)
for random_number in rand():
    a = random_number
for random_number in ran():
    b = random_number
def Names():
    name = input("What is your name?: ")
    return name
def math():
    c = a * b
    return c
def question():
    ans = int(input("What is %d * %d?: " % (a, b)))
    return ans
def incor():
    ans = question()
    c = math()
    if(ans == c):
        coi = "Correct"
        return coi
    else:
        coi = "Incorrect"
        return coi
def results():
    ans = question()
    c = math()
    coi = incor()
    name = Names()
    dict = {"Stats": ["First number", "Second number", "Your answer", "Correct answer", "Correct or incorrect"], name: [a, b, ans, c, coi]}
    res = pd.DataFrame(dict)
    return res
def printing():
    res = results()
    print(res)
printing()
