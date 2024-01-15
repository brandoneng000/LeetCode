from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        def counting_sort(nums: List[int]):
            count = [0] * (max(nums) + 1)
            res = [None] * len(nums)

            for n in nums:
                count[n] += 1

            for i in range(1, len(count)):
                count[i] += count[i - 1]
            
            for i in range(len(nums) - 1, -1, -1):
                res[count[nums[i]] - 1] = nums[i]
                count[nums[i]] -= 1
            
            return res
        
        sorted_costs = counting_sort(costs)
        
        if sorted_costs[0] > coins:
            return 0
        
        for i in range(1, len(sorted_costs)):
            sorted_costs[i] += sorted_costs[i - 1]

            if sorted_costs[i] > coins:
                return i
        
        return len(sorted_costs)


def main():
    sol = Solution()
    print(sol.maxIceCream(costs = [7,3,3,6,6,6,10,5,9,2], coins = 56))
    print(sol.maxIceCream(costs = [1,3,2,4,1], coins = 7))
    print(sol.maxIceCream(costs = [10,6,8,7,7,8], coins = 5))
    print(sol.maxIceCream(costs = [1,6,3,1,2,5], coins = 20))

if __name__ == '__main__':
    main()