def is_perm(s1, s2):
    ss1 = sorted(s1)
    ss2 = sorted(s2)
    return ss1 == ss2

def test():
    tests = [["asdasd", "daadss"], ["eeW", "ewe"], ["qweasd", "QWEASDQWE"], [" 2", ""]]
    answers = [True, False, False, False]
    flag = True
    for t, a in zip(tests, answers):
        if not is_perm(t[0], t[1]) == a:
            print("Test ", t, " failed")
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()