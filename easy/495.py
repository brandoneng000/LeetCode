from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # res = 0
        # cur = timeSeries[0]

        # for i in range(1, len(timeSeries)):
        #     res += min(timeSeries[i] - cur, duration)
        #     cur = timeSeries[i]
        
        # return res + duration

        timeSeries = [timeSeries[i + 1] - timeSeries[i] for i in range(len(timeSeries) - 1)]

        return sum(min(time, duration) for time in timeSeries) + duration
            
        
def main():
    sol = Solution()
    print(sol.findPoisonedDuration(timeSeries = [1,4], duration = 2))
    print(sol.findPoisonedDuration(timeSeries = [1,2], duration = 2))

if __name__ == '__main__':
    main()