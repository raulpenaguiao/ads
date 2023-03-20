def set_zero(mat): # This function changes the input
    l = len(mat)
    if l == 0:
        return None
    m = len(mat[0])
    rows = [False for i in range(l)]
    cols = [False for i in range(m)]
    for i in range(l):
        for j in range(m):
            if mat[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(l):
        for j in range(m):
            if cols[i] or cols[j]:
                mat[i][j] = 0
    return None

def test():
    tests = [[[1, 2, 3], [4, 0, 6], [7, 8, 9]], [[5, 6], [7, 8]], [[5, 6], [7, 0]], [[7]]]
    answers = [[[1, 0, 3], [0, 0, 0], [7, 0, 9]], [[5, 6], [7, 8]], [[5, 0], [0, 0]], [[7]]]
    flag = True
    for t, a in zip(tests, answers):
        set_zero(t)
        if not t == a:
            print("Test ", t, " failed with answer = ", None, " instead of ", a)
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()