class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to store child nodes (character -> TrieNode)
        self.is_end = False  # Marks end of a complete word



class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            # If character not present, create a new node
            if ch not in node.children: 
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, word):\
        # Helper function to traverse the trie
        node = self.root

        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]

        return node
