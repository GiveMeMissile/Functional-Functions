def test():
    return "eat dolphins", "burn worlds", "pat doggos", "feed humans to doggos"
def test2(what):
    return "I LOVE to %s" % what
def test3():
    testing = test()
    for what in testing:
        print(test2(what))
test3()
