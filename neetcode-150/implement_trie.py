"""
208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is
a tree data structure used to efficiently store and
retrieve keys in a dataset of strings.
There are various applications of this data structure,
such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true
if the string word is in the trie (i.e., was inserted before),
and false otherwise.
boolean startsWith(String prefix)
Returns true if there is a previously inserted string
word that has the prefix prefix,
and false otherwise.
"""


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur["*"] = ""

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter in cur:
                cur = cur[letter]
            else:
                return False

        return "*" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
print(obj.search("word"))
print(obj.startsWith("wosr"))
