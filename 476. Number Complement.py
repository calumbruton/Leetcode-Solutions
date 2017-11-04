class Solution(object):
    def findComplement(self, num):
        binary = str(bin(num))
        complement = []
        for char in binary[2:]:
            if char == "1":
                complement.append("0")
            else: 
                complement.append("1")
        return int("".join(complement), 2)