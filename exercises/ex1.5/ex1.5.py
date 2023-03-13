def one_d_away(s1, s2):
    i1 = 0
    i2 = 0
    flag = True
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            i1 += 1
            if not flag:
                return False
            flag = False
    if flag and i1 < len(s1):
        i1 += 1
    return i1 == len(s1) and i2 == len(s2)

def one_i_away(s1, s2):
    i1 = 0
    i2 = 0
    flag = True
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            i2 += 1
            if not flag:
                return False
            flag = False
    if flag and i2 < len(s2):
        i2 += 1
    return i1 == len(s1) and i2 == len(s2)

def one_r_away(s1, s2):
    i1 = 0
    i2 = 0
    flag = True
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            i1 += 1
            i2 += 1
            if not flag:
                return False
            flag = False
    return i1 == len(s1) and i2 == len(s2)


def one_away(s1, s2):
    return one_d_away(s1, s2) or one_r_away(s1, s2) or one_i_away(s1, s2)


def test():
    tests = [[" ", " l"], ["_l", " l"], ["kd", "d"], ["kjl", "jlk"], ["qweasd", "qwesd"], ["qweQWE", "qwewQWE"]]
    answers = [True, True, True, False, True, True]
    flag = True
    for t, a in zip(tests, answers):
        ans = one_away(t[0] ,t[1])
        if not ans == a:
            print("Test ", t, " failed with answer = ", ans)
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()