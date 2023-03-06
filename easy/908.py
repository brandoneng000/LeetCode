from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        result = max(nums) - min(nums) - k * 2 
        return result if result > 0 else 0

def main():
    sol = Solution()
    print(sol.smallestRangeI(nums = [1], k = 0))
    print(sol.smallestRangeI(nums = [0,10], k = 2))
    print(sol.smallestRangeI(nums = [1,3,6], k = 3))

if __name__ == '__main__':
    main()