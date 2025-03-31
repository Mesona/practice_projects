# https://leetcode.com/problems/can-place-flowers/submissions/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available = 0
        prev_pot = None
        next_pot = None
        for idx, pot in enumerate(flowerbed):
            curr_pot = flowerbed[idx]
            if prev_pot == None:
                prev_pot = 0
                
            if idx == len(flowerbed) - 1:
                next_pot = 0
            else:
                next_pot = flowerbed[idx + 1]
                
            if prev_pot == 0 and next_pot == 0 and curr_pot == 0:
                available += 1
                prev_pot = 1
            else:
                prev_pot = flowerbed[idx]
                
        print("N: " + str(n))
        print("Available: " + str(available))
            
        if available >= n:
            return True
        else:
            return False
                