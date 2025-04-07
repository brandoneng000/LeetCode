from typing import List
import collections

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2
        possible_sums = set([0])

        for num in nums:
            next_sums = set()

            for cur in possible_sums:
                if cur + num == target:
                    return True
                
                next_sums.add(cur + num)
            
            possible_sums.update(next_sums)
        
        return target in possible_sums


    # def canPartition(self, nums: List[int]) -> bool:
    #     total = sum(nums)
    #     if total % 2 == 1:
    #         return False
        
    #     total //= 2
    #     dp = [False] * (total + 1)
    #     dp[0] = True

    #     for n in nums:
    #         for t in range(total, -1, -1):
    #             if t >= n:
    #                 dp[t] = dp[t] or dp[t - n]
            
    #     return dp[total]

def main():
    sol = Solution()
    print(sol.canPartition([1,5,11,5]))
    print(sol.canPartition([1,2,3,5]))
    print(sol.canPartition([1,1]))
    print(sol.canPartition([2,2,1,1]))

if __name__ == '__main__':
    main()