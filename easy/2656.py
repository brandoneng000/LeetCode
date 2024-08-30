from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + (k - 1) * k // 2
        
def main():
    sol = Solution()
    print(sol.maximizeSum(nums = [1,2,3,4,5], k = 3))
    print(sol.maximizeSum(nums = [5,5,5], k = 2))

if __name__ == '__main__':
    main()