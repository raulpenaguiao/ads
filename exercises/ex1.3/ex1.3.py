def URLify(st, l):
    s = list(st)
    index = len(s)-1
    for i in range(l-1, -1, -1):
        if s[i] == " ":
            s[index] = "0"
            s[index - 1] = "2"
            s[index - 2] = "%"
            index -= 3
        else:
            s[index] = s[i]
            index -= 1
    return "".join(s[index+1:])



def test():
    tests = [["asd asd    ", 7], ["eeW", 3], ["q w e as d               ", 10], [" 2     ", 3]]
    answers = ["asd%20asd", "eeW", "q%20w%20e%20as%20d", "%202%20"]
    flag = True
    for t, a in zip(tests, answers):
        ans = URLify(t[0], t[1])
        if not ans == a:
            print("Test ", t, " failed with answer = ", ans)
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()