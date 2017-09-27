class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        retlist = []
        for word in words:
            w = set(word.lower())
            if w.issubset(s1) or w.issubset(s2) or w.issubset(s3):
                retlist.append(word)
                
        return retlist