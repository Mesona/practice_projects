# https://leetcode.com/problems/count-binary-substrings/submissions/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        repeats = 0
        current = ""
        for idx, num in enumerate(s):
            if len(current) == 0:
                current += num
                continue
                
            if num != current[-1]:
                current = current.replace(num, "")
                current += num
            else:
                current += num
                
            zeroes = current.count("0")
            ones = current.count("1")
            if num == "0" and ones >= zeroes:
                repeats += 1
            elif num == "1" and ones <= zeroes:
                repeats += 1
                          
        return repeats