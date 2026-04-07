class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Case 1: Empty Strings
        if not s and not t:
            return True
        
        #Case 2: Different String Lengths
        if len(s) != len(t):
            return False
        
        #Case 3: Same Length Strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        str_length = len(sorted_s)

        for i in range(str_length):
            if sorted_s[i] != sorted_t[i]:
                return False
        
        return True