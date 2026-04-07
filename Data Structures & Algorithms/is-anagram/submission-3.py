class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Case 1: Empty Strings
        if not s and not t:
            return True
        
        #Case 2: Different String Lengths
        if len(s) != len(t):
            return False
        
        #Case 3: Same Length Strings
        str_length = len(s)
        char_balance = {
            "a":0,
            "b":0,
            "c":0,
            "d":0,
            "e":0,
            "f":0,
            "g":0,
            "h":0,
            "i":0,
            "j":0,
            "k":0,
            "l":0,
            "m":0,
            "n":0,
            "o":0,
            "p":0,
            "q":0,
            "r":0,
            "s":0,
            "t":0,
            "u":0,
            "v":0,
            "w":0,
            "x":0,
            "y":0,
            "z":0,
        }

        for i in range(str_length):
            s_char = s[i]
            char_balance[s_char] -= 1 #encounters of s decrease character balance 
            
            t_char = t[i]
            char_balance[t_char] += 1 #encounters of t decrease character balance 
        
        for value in char_balance.values():
            if value != 0: #all character balances must be 0 to have anagram
                return False
        
        return True