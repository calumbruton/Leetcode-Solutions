
class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        print("Create Trie")

    def insert(self, word):
        curr = self.root
        for i, ch in enumerate(word):
            if not ch in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            if (i == len(word)-1):
                curr.leaf = True

    def search(self, word):
        curr = self.root
        for i, ch in enumerate(word):
            if not ch in curr.children:
                return False
            curr = curr.children[ch]
            # print(ch, curr.children, curr.leaf)
            if i == len(word)-1:
                if curr.leaf == True:
                    return True
                return False

            
    def remove(self, word):
        path = []
        curr = self.root
        path.append(curr)
        for i, ch in enumerate(word):
            if not ch in curr.children:
                return False
            curr = curr.children[ch]
            path.append(curr)

        curr.leaf = False
        # this is a path to other words making it not a leaf is enough
        if len(curr.children) > 0:
            return True

        for i, ch in enumerate(reversed(word)):
            if path[len(word)-i].leaf == False and len(path[len(word)-i-1].children) == 1:
                path[len(word)-i].children.pop(ch, None)
            else:
                return True

        return True

        

def main():
    trie = Trie()

    print("\nInsert: Hello, Help and Hell")
    trie.insert("Hello")
    trie.insert("Hello")
    trie.insert("Help")
    trie.insert("Hell")

    print("Search Hello: ", trie.search("Hello"))
    print("Search Nope: ", trie.search("Nope"))
    
    print("\nRemove Hello")
    trie.remove("Hello")
    print("Search Hello: ", trie.search("Hello"))
    print("Search Help: ", trie.search("Help"))
    print("Search Hell: ", trie.search("Hell"))

    print("\nRemove Hell:", trie.remove("Hell"))
    print("Search Hell: ", trie.search("Hell"))
    print("Search Hello: ", trie.search("Hello"))


main()
