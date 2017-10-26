class Solution(object):
    def maxProduct(self, words):
        """Solution taken from discussion
            Using bitwise operations
        """
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
                #print(w, c, bin(mask))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
        
        
        
        """
        Solution O(n^2) - times out
        
        # Sort the list of words by length descending
        words.sort(key = len, reverse=True)
        largest = 0
        for i, word in enumerate(words):
            # For efficiency break the loop if the word times itself is not possibly longer since they are sorted
            if (len(word)*len(word)) < largest:
                break
            letters1 = set(word)
            found = False
            while i<len(words)-1 and not found:
                word2 = words[i+1]
                letters2 = set(word2)
                if letters1 & letters2 == set():
                    if (len(word) * len(word2)) > largest:
                        largest = (len(word) * len(word2))
                    found = True
                i += 1
        
        
        return largest
        """