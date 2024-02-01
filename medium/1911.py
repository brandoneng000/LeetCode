from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even, odd = 0, 0

        for num in nums:
            even, odd = max(even, odd + num), max(odd, even - num)
        
        return even


def main():
    sol = Solution()
    print(sol.maxAlternatingSum([4,2,5,3]))
    print(sol.maxAlternatingSum([5,6,7,8]))
    print(sol.maxAlternatingSum([6,2,1,2,4,5]))

if __name__ == '__main__':
    main()