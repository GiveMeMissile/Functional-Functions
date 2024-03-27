import random
def test():
    for i in range(1):
        yield random.randint(1,50)
for random_number in test():
    def test2():
        a = random_number
        return a
    for random_number in tests():
        def test3():
            b = random_number
            return b
        def test4():
            c = test3()
            d = test2()
            tell = int(input("What is %d + %d?: " % (c, d)))
            return tell
        def test5():
            tell2 = test4()
            f = test3()
            g = test2()
            e = g + f
            if(e == tell2):
                print("Correct")
            else:
                print("Incorrect. The answer was %d" % e)
        test5()
