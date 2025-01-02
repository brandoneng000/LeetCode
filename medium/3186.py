from typing import List
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power_count = Counter(power)
        power_set = sorted(power_count)
        n = len(power_set)
        dp = [0] * n
        dp[0] = power_set[0] * power_count[power_set[0]]

        for i in range(1, n):
            cur_power = power_set[i]
            total_power = cur_power * power_count[cur_power]
            dp[i] = dp[i - 1]

            prev_index = i - 1

            while prev_index >= 0 and (
                    power_set[prev_index] == cur_power - 1 or
                    power_set[prev_index] == cur_power - 2 or
                    power_set[prev_index] == cur_power + 1 or
                    power_set[prev_index] == cur_power + 2
                ):
                prev_index -= 1

            if prev_index >= 0:
                dp[i] = max(dp[i], dp[prev_index] + total_power)
            else:
                dp[i] = max(dp[i], total_power)
            
        return dp[n - 1]

        
def main():
    sol = Solution()
    print(sol.maximumTotalDamage([1,1,3,4]))
    print(sol.maximumTotalDamage([7,1,6,6]))

if __name__ == '__main__':
    main()