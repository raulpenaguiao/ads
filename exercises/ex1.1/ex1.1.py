def has_all_unique(str):
    n_str = sorted(str)
    for k in range(len(n_str) - 1):
        if n_str[k] == n_str[k+1]:
            return False
    return True



def test():
    tests = ["asdasd", "qweasd", "QWEASDQWE", " 2"]
    answers = [False, True, False, True]
    flag = True
    for t, a in zip(tests, answers):
        if not has_all_unique(t) == a:
            print()
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()