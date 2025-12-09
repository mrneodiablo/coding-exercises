"""
211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if
a string matches any previously added string.

Implement the WordDictionary class:
    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure,
    it can be matched later.
    bool search(word) Returns true if there is any string in
    the data structure that
    matches word or false otherwise.
    word may contain dots '.' where dots can be matched with any letter.


Example:

Input
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
    [null,null,null,null,false,true,true,true]

Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True
"""


class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current = self.root
        for w in word:
            if w not in current:
                current[w] = {}

            current = current[w]

        current["*"] = 1

    def search(self, word: str) -> bool:
        """
        Search for a word in the trie.
        '.' can match any single character.
        """

        def dfs(node: dict, index: int) -> bool:
            # Base case: reached end of word
            if index == len(word):
                return "*" in node

            char = word[index]

            # Case 1: Wildcard '.' - try all possible characters
            if char == ".":
                for key in node:
                    if key != "*" and dfs(node[key], index + 1):
                        return True
                return False

            # Case 2: Regular character - direct lookup
            if char not in node:
                return False
            return dfs(node[char], index + 1)

        return dfs(self.root, 0)


s = WordDictionary()
s.addWord("aa")
s.addWord("ba")

print(s.search("ba"))
print(s.search("b."))
print(s.search(".."))
