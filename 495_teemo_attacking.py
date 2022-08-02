# 495. Teemo Attacking

from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalDuration = duration
        poisonUntil = timeSeries[0] + duration - 1
        
        for t in timeSeries[1:]: # O(n)
            if t > poisonUntil:
                totalDuration += duration
            else:
                totalDuration += duration - (poisonUntil - t) - 1
            
            poisonUntil = max(poisonUntil, t + duration - 1)
                    
        return totalDuration