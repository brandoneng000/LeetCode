from typing import List
from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        
        if n > ceil(hour):
            return -1
        
        slow = 1
        fast = 10000000

        while slow <= fast:
            average = (slow + fast) // 2
            time_traveled = sum(ceil(dist[i] / average) for i in range(n - 1))
            time_traveled += dist[-1] / average
            if hour < time_traveled:
                slow = average + 1
            else:
                fast = average - 1
        
        return ceil(slow)


def main():
    sol = Solution()
    print(sol.minSpeedOnTime(dist = [1,1,100000], hour = 2.01))
    print(sol.minSpeedOnTime(dist = [1,3,2], hour = 6))
    print(sol.minSpeedOnTime(dist = [1,3,2], hour = 2.7))
    print(sol.minSpeedOnTime(dist = [1,3,2], hour = 1.9))

if __name__ == '__main__':
    main()