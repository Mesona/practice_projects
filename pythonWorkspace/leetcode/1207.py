# https://leetcode.com/problems/unique-number-of-occurrences/submissions/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = set([arr.count(i) for i in arr])
        return len(occur) == len(set(arr))