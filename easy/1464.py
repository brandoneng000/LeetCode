from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = max(nums)
        nums.remove(first)
        return (first - 1) * (max(nums) - 1)

def main():
    sol = Solution()
    print(sol.maxProduct([3,4,5,2]))
    print(sol.maxProduct([1,5,4,5]))
    print(sol.maxProduct([3,7]))

if __name__ == '__main__':
    main()