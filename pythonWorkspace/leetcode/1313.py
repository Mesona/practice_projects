https://leetcode.com/problems/decompress-run-length-encoded-list/submissions/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        array_length = 0
        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                array_length = num
            else:
                result += [num for i in range(array_length)]
                array_length = 0
                
        return result