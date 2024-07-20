from typing import List

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0

        for i in range(n // 2 - 1, -1, -1):
            left = i * 2 + 1
            right = i * 2 + 2

            res += abs(cost[left] - cost[right])
            cost[i] += max(cost[left], cost[right])
        
        return res

    # def minIncrements(self, n: int, cost: List[int]) -> int:
    #     def helper(nums: List[int], goal: int):
    #         n = len(nums)

    #         if n == 1:
    #             return goal - nums[0]

    #         diff = min([goal - nums[i] for i in range(n)])
            
    #         return diff + helper(nums[:n // 2], goal - diff) + helper(nums[n // 2:], goal - diff)

    #     levels = bin(n).count('1')

    #     for i in range(1, n + 1):
    #         if 2 * i > n:
    #             break
            
    #         cost[2 * i - 1] += cost[i - 1]
    #         cost[2 * i] += cost[i - 1]
        
    #     res = cost[-2 ** (levels - 1):]

    #     return helper(cost[-2 ** (levels - 1):], max(res))        

def main():
    sol = Solution()
    print(sol.minIncrements(n = 7, cost = [1,5,2,2,3,3,1]))
    print(sol.minIncrements(n = 3, cost = [5,3,3]))

if __name__ == '__main__':
    main()
