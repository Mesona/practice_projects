# https://leetcode.com/problems/split-a-string-in-balanced-strings/submissions/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L = 0
        R = 0
        output = 0
        for i in s:
            if i == "L":
                L = L + 1
            
            if i == "R":
                R = R + 1
                
            if R == L:
                L = 0
                R = 0
                output = output + 1
        
        return output