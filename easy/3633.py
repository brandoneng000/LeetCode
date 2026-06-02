from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        res = 10 ** 33

        for i in range(n):
            for j in range(m):
                land_start = landStartTime[i]
                land_dur = landDuration[i]
                water_start = waterStartTime[j]
                water_dur = waterDuration[j]

                cur_time = land_start + land_dur
                cur_time = max(cur_time, water_start) + water_dur
                res = min(res, cur_time)

                cur_time = water_start + water_dur
                cur_time = max(cur_time, land_start) + land_dur
                res = min(res, cur_time)
        
        return res
        
def main():
    sol = Solution()
    print(sol.earliestFinishTime(landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]))
    print(sol.earliestFinishTime(landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]))

if __name__ == '__main__':
    main()