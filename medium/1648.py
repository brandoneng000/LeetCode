from typing import List
from collections import Counter

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def helper(b: int):
            sold = 0

            for ball in inventory:
                sold += max(0, ball - b)
            
            return sold
        
        mod = 1000000007
        left, right = 0, max(inventory)
        res = 0

        while left < right:
            middle = (left + right + 1) // 2
            
            if helper(middle) >= orders:
                left = middle
            else:
                right = middle - 1
        
        res = sum((b + left + 1) * (b - left) // 2 for b in inventory if b > left)

        return (res - (helper(left) - orders) * (left + 1)) % mod 




def main():
    sol = Solution()
    print(sol.maxProfit(inventory = [2,5], orders = 4))
    print(sol.maxProfit(inventory = [3,5], orders = 6))

if __name__ == '__main__':
    main()