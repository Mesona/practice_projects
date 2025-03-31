# https://leetcode.com/problems/remove-outermost-parentheses/submissions/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        parans_nums = 0
        result = ""
        for char in S:
            if char == "(":
                if parans_nums > 0:
                    result += char
                    parans_nums += 1
                else:
                    parans_nums += 1
            else:
                if parans_nums == 1:
                    parans_nums += -1
                else:
                    parans_nums += -1
                    result += char
        
        return result