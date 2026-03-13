from typing import List
from heapq import heappush, heappop

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = len(workerTimes)
        heap = []
        cur_time = [0] * n

        for index, work in enumerate(workerTimes):
            heappush(heap, (work, work, 2, index))

        while mountainHeight:
            work, add_time, times_worked, index = heappop(heap)
            cur_time[index] = workerTimes[index]
            workerTimes[index] += add_time * times_worked
            heappush(heap, (workerTimes[index], add_time, times_worked + 1, index))

            mountainHeight -= 1

        return max(cur_time)
            
def main():
    sol = Solution()
    print(sol.minNumberOfSeconds(mountainHeight = 10, workerTimes = [1,1000000,1000000,1000000]))
    print(sol.minNumberOfSeconds(mountainHeight = 4, workerTimes = [2,1,1]))
    print(sol.minNumberOfSeconds(mountainHeight = 10, workerTimes = [3,2,2,4]))
    print(sol.minNumberOfSeconds(mountainHeight = 5, workerTimes = [1]))

if __name__ == '__main__':
    main()