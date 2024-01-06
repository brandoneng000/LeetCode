from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        cache = {}
        
        def dfs(i: int):
            if i == n:
                return 0
            
            if i in cache:
                return cache[i]
            
            res = dfs(i + 1)
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))

            res = max(res, jobs[i][2] + dfs(j))
            cache[i] = res
            return res
        
        return dfs(0)

        
def main():
    sol = Solution()
    print(sol.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
    print(sol.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
    print(sol.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))

if __name__ == '__main__':
    main()