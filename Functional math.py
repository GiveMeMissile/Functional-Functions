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
        if(x == 1):
            a1 = a
            b1 = b
            c1 = c
            pa1 = pa
            ic = corrin()
            x += 1
        else:
            if(x == 2):
                a2 = a
                b2 = b
                c2 = c
                pa2 = pa
                ic2 = corrin()
                x += 1
            else:
                if(x == 3):
                    a3 = a
                    b3 = b
                    c3 = c
                    pa3 = pa
                    ic3 = corrin()
                    x += 1
                else:
                    if(x == 4):
                        a4 = a
                        b4 = b
                        c4 = c
                        pa4 = pa
                        ic4 = corrin()
                        x += 1
                    else:
                        if(x == 5):
                            a5 = a
                            b5 = b
                            c5 = c
                            pa5 = pa
                            ic5 = corrin()
                            x += 1
                        else:
                            
