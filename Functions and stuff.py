def test():
    name = input("What is your name?: ")
    return "Hello %s, How is your day going?: " % name
def after():
    test2 = test()
    day = input(test2)
    print("Its wonderful that your day was %s!!!" % (day))
after()
