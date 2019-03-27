"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
import collections


class TrieNode:
    def __init__(self):
        self.children = dict()
        # self.char_str = None
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for i in word:
            if p.children.get(i) is None:
                a = TrieNode()
                a.char_str = i
                p.children[i] = a

            p = p.children[i]
        p.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for letter in word:
            p = p.children.get(letter)
            if p is None:
                return False

        return p.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for letter in prefix:
            p = p.children.get(letter)
            if p is None:
                return False

        return True



# Your Trie object will be instantiated and called as such:
word = "apple"
prefix = "app"

obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
print(obj.search("aaa"))
param_3 = obj.startsWith(prefix)
print(param_3)
