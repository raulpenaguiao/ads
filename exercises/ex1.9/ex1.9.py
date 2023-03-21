
def isSubstring(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    for i in range(l2-l1):
        flag = True
        for index, c, in enumerate(str1):
            if not c == str2[index+i]:
                flag = False
        if flag:
            return True
    return False

def string_rotation(str1, str2):
    if not len(str1) == len(str2):
        return False
    return isSubstring(str1, str2+str2)


def test():
    tests = [["abc", "acb"], ["waterbottle", "tlewaterbot"], ["aaaaaaaabaaa", "aabaaaaaaaaa"]]
    answers = [False, True, True]
    flag = True
    for t, a in zip(tests, answers):
        ans = string_rotation(t[0], t[1])
        if not ans == a:
            print("Test ", t, " failed with answer = ", ans, " instead of ", a)
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()