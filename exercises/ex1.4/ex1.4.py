import sys
sys.path.insert(1, '/home/penegas/projects/prog/python/learning/ads/hash_table/')
from hash_table import Hash_Table

def palindrome_permutations(st):
    ht = Hash_Table()
    for c in st:
        if ht.has_key(c):
            ht.insert(c, ht.fetch(c)+1)
        else:
            ht.insert(c, 1)
    flag = False
    for k in ht.keys():
        if not k == " ":
            if ht.fetch(k)%2 == 1:
                if flag:
                    return False
                flag = True
    return True
            

def test():
    tests = [" true teucr", "tact cat", " toct cat", "fase swafer", "fase safe", "lp"]
    answers = [True, True, False, False, True, False]
    flag = True
    for t, a in zip(tests, answers):
        ans = palindrome_permutations(t)
        if not ans == a:
            print("Test ", t, " failed with answer = ", ans)
            flag = False
    if flag:
        print("There were no errors, the function passed all the tests successfully")

test()