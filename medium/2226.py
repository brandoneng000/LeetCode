from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def split_candies(candies: List[int], amount: int):
            return sum(c // amount for c in candies)
        
        if sum(candies) < k:
            return 0
        
        left, right = 1, max(candies)

        while left < right:
            middle = (left + right + 1) // 2

            if split_candies(candies, middle) >= k:
                left = middle
            else:
                right = middle - 1
        
        return left
        
        
def main():
    sol = Solution()
    print(sol.maximumCandies(candies = [5,6,4,10,10,1,1,2,2,2], k = 9))
    print(sol.maximumCandies(candies = [5,8,6], k = 3))
    print(sol.maximumCandies(candies = [2,5], k = 11))

if __name__ == '__main__':
    main()