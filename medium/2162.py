from typing import List

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def check_cost(time: str, start: str):
            res = 0

            for digit in time:
                if start == digit:
                    res += pushCost
                else:
                    start = digit
                    res += moveCost + pushCost
            
            return res
        
        times = []

        if targetSeconds <= 99:
            times.append(str(targetSeconds))

        minute, second = targetSeconds // 60, targetSeconds % 60

        if minute <= 99 and second <= 99:
            times.append(str(minute) + str(second).zfill(2))

        if minute > 1 and minute - 1 <= 99 and second <= 39:
            times.append(str(minute - 1) + str(second + 60).zfill(2))
        
        return min(check_cost(t, str(startAt)) for t in times)

        
def main():
    sol = Solution()
    print(sol.minCostSetTime(startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600))
    print(sol.minCostSetTime(startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76))

if __name__ == '__main__':
    main()