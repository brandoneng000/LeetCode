from typing import List
from collections import deque

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def helper(cur_cost: int, toppings: List[int], index: int, target: int):
            if abs(target - cur_cost) < abs(target - self.res) or (abs(target - cur_cost) == abs(target - self.res) and cur_cost < self.res):
                self.res = cur_cost
            if index == len(toppings) or cur_cost >= target:
                return
            helper(cur_cost, toppings, index + 1, target)
            helper(cur_cost + toppings[index], toppings, index + 1, target)
            helper(cur_cost + toppings[index] * 2, toppings, index + 1, target)

        self.res = baseCosts[0]
        for b in baseCosts:
            helper(b, toppingCosts, 0, target)
        
        return self.res


        
def main():
    sol = Solution()
    print(sol.closestCost(baseCosts = [1,7], toppingCosts = [3,4], target = 10))
    print(sol.closestCost(baseCosts = [2,3], toppingCosts = [4,5,100], target = 18))
    print(sol.closestCost(baseCosts = [3,10], toppingCosts = [2,5], target = 9))

if __name__ == '__main__':
    main()