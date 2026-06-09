from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k
        
def main():
    sol = Solution()
    print(sol.maxTotalValue(nums = [1,3,2], k = 2))
    print(sol.maxTotalValue(nums = [4,2,5,1], k = 3))

if __name__ == '__main__':
    main()