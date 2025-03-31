# https://leetcode.com/problems/defanging-an-ip-address/submissions/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        for addr in address:
            if addr == ".":
                defanged += "[.]"
            else:
                defanged += addr
                
        return defanged