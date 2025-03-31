# https://leetcode.com/problems/maximum-69-number/submissions/

class Solution:
    def maximum69Number (self, num: int) -> int:
        final_num = ""
        swapped = "false"
        for i in str(num):
            if  i == "6" and swapped == "false":
                final_num += "9"
                swapped = "true"
            else:
                final_num += i
                
        return int(final_num)