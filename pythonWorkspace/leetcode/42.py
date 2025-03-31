#https://leetcode.com/problems/trapping-rain-water/submissions/

class Solution:
    def trap(self, height: List[int]) -> int:
        stored_water = 0
        current_height = []
        one_run = False
        for i, val in enumerate(height):
            if len(current_height) > 0 and height[i] >= current_height[0]:
                stored_water = stored_water + self.calcWater(current_height)
                if i == len(height) - 1:
                    one_run = True
                    
                current_height = [height[i]]
            else:
                current_height.append(height[i])
           
        if one_run == False:
            current_height.reverse()
            height = current_height
            current_height = []
            for i in height:
                if len(current_height) > 0 and i >= current_height[0]:
                    stored_water += self.calcWater(current_height)
                    current_height = [i]
                else:
                    current_height.append(i)
                
        return stored_water
                
    def calcWater(self, arr):
        land = sum(arr)
        max_water = arr[0] * len(arr)
        return max_water - land
            
        