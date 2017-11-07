class Solution(object):
    def groupAnagrams(self, strs):
        anas = {}
        for word in strs:
            keyword = "".join(sorted(word))
            if keyword in anas:
                anas[keyword].append(word)
            else:
                anas[keyword] = [word]
        
        return list(anas.values())
        