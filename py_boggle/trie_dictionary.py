import typing
from typing import Optional, Dict
from collections.abc import Iterator

from py_boggle.boggle_dictionary import BoggleDictionary


class TrieNode:
    """
    Our TrieNode class. Feel free to add new properties/functions, but
    DO NOT edit the names of the given properties (children and is_word).
    """
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}  # Child letter to TrieNode
        self.is_word: bool = False  # Is this node a valid word ending?

class TrieDictionary(BoggleDictionary):
    """
    Your implementation of BoggleDictionary.
    Several functions have been filled in for you from our solution, but you are free to change their implementations.
    Do NOT change the name of self.root, as our autograder will manually traverse using self.root
    """

    def __init__(self):
        self.root : TrieNode = TrieNode()

    def load_dictionary(self, filename: str) -> None:
        # Remember to add every word to the trie, not just the words over some length.
        with open(filename) as wordsfile:
            for line in wordsfile:
                word = line.strip().lower()
                curr = self.root
                for ch in word:
                    if ch not in curr.children:
                        curr.children[ch] = TrieNode()
                    curr = curr.children[ch]
                curr.is_word = True

    def traverse(self, prefix: str) -> Optional[TrieNode]:
        """
        Traverse will traverse the Trie down a given path of letters `prefix`.
        If there is ever a missing child node, then returns None.
        Otherwise, returns the TrieNode referenced by `prefix`.
        """
        curr = self.root
        for ch in prefix.lower():
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return curr

    def is_prefix(self, prefix: str) -> bool:
        return self.traverse(prefix) is not None

    def contains(self, word: str) -> bool:
        node = self.traverse(word)
        return node is not None and node.is_word

    def __iter__(self) -> typing.Iterator[str]:
        def dfs(node: TrieNode, prefix: str):
            if node.is_word:
                yield prefix
            for ch, child in node.children.items():
                yield from dfs(child, prefix + ch)
        yield from dfs(self.root, "")