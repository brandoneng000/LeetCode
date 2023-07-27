from typing import List
import heapq

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n

        while left < right:
            target = right - (right - left) // 2

            extra = 0
            for power in batteries:
                extra += min(power, target)

            if extra // n >= target:
                left = target
            else:
                right = target - 1
            
        return left

    # def maxRunTime(self, n: int, batteries: List[int]) -> int:
    #     batteries.sort()
    #     extra_power = sum(batteries[:-n])

    #     cur_power = batteries[-n:]

    #     for i in range(n - 1):
    #         if extra_power // (i + 1) < cur_power[i + 1] - cur_power[i]:
    #             return cur_power[i] + extra_power // (i + 1)

    #         extra_power -= (i + 1) * (cur_power[i + 1] - cur_power[i])
        
    #     return cur_power[-1] + extra_power // n
        

    # def maxRunTime(self, n: int, batteries: List[int]) -> int:
    #     heap = []
    #     res = 0
        
    #     for battery in batteries:
    #         heapq.heappush(heap, -battery)

    #     while len(heap) >= n:
    #         cur_batteries = []
    #         res += 1

    #         for _ in range(n):
    #             battery = heapq.heappop(heap)
    #             battery += 1
    #             if battery != 0:
    #                 cur_batteries.append(battery)
            
    #         for battery in cur_batteries:
    #             heapq.heappush(heap, battery)
        
    #     return res

def main():
    sol = Solution()
    print(sol.maxRunTime(n = 2, batteries = [3,3,3]))
    print(sol.maxRunTime(n = 2, batteries = [1,1,1,1]))

if __name__ == '__main__':
    main()