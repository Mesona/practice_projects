# https://leetcode.com/problems/longest-palindromic-substring/submissions/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        palindrome = ""
        for idx1, i in enumerate(s):
            for idx2, j in enumerate(s[idx1:]):
                word = s[idx1:idx1 + idx2 + 1]
                if word == word[::-1] and len(word) > len(palindrome):
                    palindrome = word
                    
        return palindrome
                
                
        