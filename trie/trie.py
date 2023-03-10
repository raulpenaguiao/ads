##Author: RAUL PENAGUIAO
##When? 10th March 2023
##Data structure of Trie with the capability of searching prefixes of words

class Trie:
    def __init__(self, words = [], node_value = "_"):
        self.node_value = node_value
        self.children = {}
        ## Creates a trie with a list of words
        ## We do not allow for the words to have the character "*"
        ## This Trie structure ignores double words
        dic = {}
        for word in words:
            if word == "":
                add_to_dic(dic, "*", 1)
            else:
                add_to_dic(dic, word[0], [word[1:]])
        for c in dic:
            if c == "*":
                for _ in range(dic["*"]):
                    self.children["*"]=Trie([], "*")
            else:
                self.children[c] = Trie(dic[c], c)


    def print_Trie(self):
        print(self.node_value, " -> ", [self.children[c].node_value for c in self.children])
        for c in self.children:
            self.children[c].print_Trie()

    def substring(self, string):
        #Gives the node of the trie that results from following the string in the tree
        #When no word has such prefix, returns trie for the largest common prefix, as well as the remaning string
        #When some word has a prefix, returns the trie for the prefix and the empty string
        ## This method does not change the trie
        if string == "":
            return [self, ""]
        if string[0] in self.children:
            a, b = self.children[string[0]].substring(string[1:])
            return [a, b]
        return [self, string]


    def append_word(self, word):
        #changes the current trie with a word appended
        T, s = self.substring(word)
        if not s == "":
            T.children[s[0]] = Trie([s[1:]], s[1])

def add_to_dic(d, ind, it):
    if ind in d:
        d[ind] += it
    else:
        d[ind] = it

words = ["Mississipi", "Missouri", "Miss", "Madam"]
T = Trie()
for word in words:
    T.append_word(word)
T.print_Trie()
