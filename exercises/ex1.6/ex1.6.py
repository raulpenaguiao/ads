def str_compression(s):
    if s == "":
        return s
    ans = ""
    l = len(s)
    count = 1
    for i in range(l-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            ans += s[i] + str(count)
            count = 1
    ans += s[-1] + str(count)
    if len(ans) < l:
        return ans
    return s

def test():
    tests = ["   ", "asdsa", "aaaddaaa", ""]
    answers = [" 3", "asdsa", "a3d2a3", ""]
    flag = True
    for t, a in zip(tests, answers):
        ans = str_compression(t)
        if not ans == a:
            print("Test ", t, " failed with answer = ", ans)
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()