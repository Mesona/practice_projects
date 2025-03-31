# https://leetcode.com/problems/teemo-attacking/submissions/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned_time = 0
        for idx, time in enumerate(timeSeries):
            if idx == len(timeSeries) - 1:
                poisoned_time += duration
            else:
                time_diff = timeSeries[idx + 1] - timeSeries[idx]
                if time_diff >= duration:
                    poisoned_time += duration
                else:
                    poisoned_time += time_diff
                    
        return poisoned_time