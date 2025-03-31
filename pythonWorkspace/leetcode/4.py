# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mix = nums1
        mix += nums2
        mix.sort()
        half = len(mix) / 2
        if len(mix) % 2 == 0:
            avg = (mix[int(half)] + mix[int(half) - 1]) / 2
            return float(avg)
        else:
            return float(mix[int(half)])
        