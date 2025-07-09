from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0
        total = [0] * (n + 1)

        for i in range(n):
            total[i + 1] = total[i] + endTime[i] - startTime[i]
        
        for i in range(k - 1, n):
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            res = max(res, right - left - (total[i + 1] - total[i - k + 1]))
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]))
    print(sol.maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]))
    print(sol.maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]))

if __name__ == '__main__':
    main()