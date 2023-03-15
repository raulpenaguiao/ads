def matrix_rotate(mat):#I'm not sure if I should change mat in place or return mat, so I am just returning mat.
    m = len(mat)
    for i in range((m+1)//2):
        for j in range(m//2):
            a = mat[i][j]
            mat[i][j] = mat[m-j-1][i]
            mat[m-j-1][i] = mat[m-i-1][m-j-1]
            mat[m-i-1][m-j-1] = mat[j][m-i-1]
            mat[j][m-i-1] = a
    return mat

def test():
    tests = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[5, 6], [7, 8]], [[7]]]
    answers = [[[7, 4, 1], [8, 5, 2], [9, 6, 3]], [[7, 5], [8, 6]], [[7]]]
    flag = True
    for t, a in zip(tests, answers):
        ans = matrix_rotate(t)
        if not ans == a:
            print("Test ", t, " failed with answer = ", ans, " instead of ", a)
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()