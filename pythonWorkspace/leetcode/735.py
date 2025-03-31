# https://leetcode.com/problems/asteroid-collision/submissions/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ongoing = True
        while ongoing and len(asteroids) > 1:
            ongoing = False
                
            for i, asteroid in enumerate(asteroids):
                if i == len(asteroids) - 1:
                    continue
                    
                first = asteroids[i]
                second = asteroids[i + 1]
                if (first > 0) and (second < 0):
                    asteroids[i] = 0
                    if first > (second * -1):
                        asteroids[i + 1] = first
                    elif (second * -1) > first:
                        asteroids[i + 1] = second
                    else:
                        asteroids[i + 1] = 0
                            
                    ongoing = True
                    
            asteroids = list(filter(lambda el: el != 0, asteroids))
        
        return asteroids
                            