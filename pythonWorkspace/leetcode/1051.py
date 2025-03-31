class Solution:
    def heightChecker(self, heights: List[int]) -> int:
      proper_heights = heights.copy()
      proper_heights.sort()
      
      moved = 0
      for i in range(len(heights)):
        if heights[i] != proper_heights[i]:
          moved += 1
          
      return moved
